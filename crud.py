"""CRUD operations."""

from model import db, connect_to_db, SavedPlaylist

import os
import base64
import requests
import logging
import time
import json

# Ref: https://medium.com/analytics-vidhya/discoverdaily-a-flask-web-application-built-with-the-spotify-api-and-deployed-on-google-cloud-6c046e6e731b


SPOTIFY_CLIENT_ID = os.environ['SPOTIFY_CLIENT_ID']
SPOTIFY_SECRET = os.environ['SPOTIFY_SECRET']

###########################
###   Token Operations  ###
###########################

def getToken(code): 
    """Get a token using the given authentication code upon Spotify sign in."""

    token_url = 'https://accounts.spotify.com/api/token'
    redirect_uri = 'http://0.0.0.0:5000/callback'

    headers = {'Accept': 'application/json', 'Content-Type': 'application/x-www-form-urlencoded'}
    body = {'code': code, 'redirect_uri': redirect_uri, 
            'grant_type': 'authorization_code', 
            'client_id': SPOTIFY_CLIENT_ID,
            'client_secret': SPOTIFY_SECRET}
    post_response = requests.post(token_url,headers=headers,data=body)
    
    if post_response.status_code == 200:
        pr = post_response.json()
        return pr['access_token'], pr['refresh_token'], pr['expires_in']
    else:
        logging.error('getToken:' + str(post_response.status_code))
        return None
    

def refreshToken(refresh_token):
    """Refresh a user's Spotify token."""

    token_url = 'https://accounts.spotify.com/api/token'

    headers = {
        'Accept': 'application/json', 'Content-Type': 'application/x-www-form-urlencoded'}
    body = {
        'refresh_token': refresh_token, 
        'grant_type': 'refresh_token', 
        'client_id': SPOTIFY_CLIENT_ID, 
        'client_secret': SPOTIFY_SECRET}
    post_response = requests.post(token_url, headers=headers, data=body)

	# 200 code indicates access token was properly granted
    if post_response.status_code == 200:
        return post_response.json()['access_token'], post_response.json()['expires_in']
    else:
        logging.error('refreshToken:' + str(post_response.status_code))
        return None


def checkTokenStatus(session):
    """Check if token is expired.  If it is, refresh token."""
    
    if time.time() > session['token_expiration']:
        # token has expired, refresh token
        payload = refreshToken(session['refresh_token'])

        if payload:
            session['token'] = payload[0]
            session['token_expiration'] = time.time() + payload[1]
        
        else: 
            logging.error('checkTokenStatus')
            return None

    return "Success"


#####################################
###    General REST Operations    ###
#####################################
  
def getReq(session, url, params={}):
    """Format and perform get requests with user token."""

    headers = {'Authorization': f'Bearer {session["token"]}'}
    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        return response.json()

    elif response.status_code == 401 and checkTokenStatus(session) != None:
        return getReq(session, url, params)

    else:
        logging.error('getReq:' + str(response.status_code))
        return None


def postReq(session, url, data):
    """Format and perform post requests with user token."""

    headers = {'Authorization': f'Bearer {session["token"]}',
                'Accept': 'application/json',
                'Content-Type': 'application/json'
              }
    response = requests.post(url, headers=headers, data=data)

    # 201: successful response with body
    # 204: successful response without body
    if response.status_code == 201:  
        return response.json()
    if response.status_code == 204:
        return response

    # 401 error; check if token is still valid and update if needed
    elif response.status_code == 401 and checkTokenStatus(session) != None:
        return postReq(session, url, data)
    elif response.status_code == 403 or response.status_code == 404:
        return response.status_code
    else:
        logging.error('postReq:' + str(response.status_code))
        return None

    
#####################################
###   User & Playlist Operations  ###
#####################################

def getUserInfo(session):
    """Get basic user info."""

    url = 'https://api.spotify.com/v1/me'
    payload = getReq(session, url)
    
    if payload == None:
        return None

    return payload


def getPlaylists(session):
    """Get a list of a user's playlists."""

    url = 'https://api.spotify.com/v1/me/playlists'
    payload = getReq(session, url)

    if payload == None:
        return None

    return payload


def getTracks(session, playlist_id):
    """Get tracks for a playlist."""

    url = f'https://api.spotify.com/v1/playlists/{playlist_id}/tracks'
    payload = getReq(session, url)

    if payload == None:
        return None

    return payload


def createPlaylist(session, playlist_name):
    """Create a new playlist."""
    
    user_id = session['user_id']
    url = f'https://api.spotify.com/v1/users/{user_id}/playlists'
    data = {'name': playlist_name}

    payload = postReq(session, url, json.dumps(data))

    if payload == None:
        return None

    return payload


def storeSavedPlaylist(user_id, orig_playlist_id, saved_playlist_id, interval):
    """Store a record of what playlists should be saved."""

    savedPlaylist = SavedPlaylist(
        user_id = str(user_id),
        orig_playlist_id = orig_playlist_id,
        saved_playlist_id = saved_playlist_id,
        interval = interval
    )

    db.session.add(savedPlaylist)
    db.session.commit()

    return savedPlaylist


def addTracksToPlaylist(session, playlist_id, track_uris):
    """Add tracks to a playlist."""

    url = f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks"
    data = track_uris

    payload = postReq(session, url, data)

    if payload == None: 
        return None
    
    return payload


def updatePlaylist(session, orig_playlist_id, saved_playlist_id):
    """Update a playlist by copying over songs from another playlist."""

    tracks = getTracks(session, orig_playlist_id)

    track_uris = {"uris": []}

    for track in tracks['items']: 
        track_uris["uris"].append(track["track"]["uri"])

    return addTracksToPlaylist(session, saved_playlist_id, json.dumps(track_uris))
    


if __name__ == '__main__':
    from server import app
    connect_to_db(app)