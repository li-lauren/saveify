"""CRUD operations."""

from model import db, connect_to_db

import os
import base64
import requests
import logging
import time

# Ref: https://medium.com/analytics-vidhya/discoverdaily-a-flask-web-application-built-with-the-spotify-api-and-deployed-on-google-cloud-6c046e6e731b


SPOTIFY_CLIENT_ID = os.environ['SPOTIFY_CLIENT_ID']
SPOTIFY_SECRET = os.environ['SPOTIFY_SECRET']

def getToken(code): 
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


def getReq(session, url, params={}):
    headers = {'Authorization': f'Bearer {session["token"]}'}
    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        return response.json()

    elif response.status_code == 401 and checkTokenStatus(session) != None:
        return getReq(session, url, params)

    else:
        logging.error('getReq:' + str(response.status_code))
        return None

def getUserInfo(session):
    url = 'https://api.spotify.com/v1/me'
    payload = getReq(session, url)
    
    if payload == None:
        return None

    return payload


def getPlaylists(session):
    url = 'https://api.spotify.com/v1/me/playlists'
    payload = getReq(session, url)

    if payload == None:
        return None

    return payload


if __name__ == '__main__':
    from server import app
    connect_to_db(app)