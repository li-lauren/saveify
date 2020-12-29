from flask import (Flask, render_template, request, flash, session,
                   redirect, jsonify, make_response)

import os
from model import connect_to_db
import crud

import urllib
import logging
import time

SECRET_KEY = os.environ['SECRET_KEY']
SPOTIFY_CLIENT_ID = os.environ['SPOTIFY_CLIENT_ID']
SPOTIFY_SECRET = os.environ['SPOTIFY_SECRET']

app = Flask(__name__)
app.secret_key = SECRET_KEY

@app.route('/')
def index():
    """Render Home Paage"""
    return render_template('index.html')

@app.route('/authorize')
def authorize():
    """Redirect to Spotify OAuth to auntheticate a user."""
    scopes = 'playlist-modify-public playlist-modify-private playlist-read-private playlist-read-collaborative user-read-email user-read-private'

    spotify_authorize_url = 'https://accounts.spotify.com/authorize?'
    params = {
        'response_type': 'code', 
        'client_id': SPOTIFY_CLIENT_ID,
        'redirect_uri': 'http://0.0.0.0:5000/callback',
        'scope': scopes
    }

    query_params = urllib.parse.urlencode(params)
    response = make_response(redirect(spotify_authorize_url + query_params))
    return response

@app.route('/callback')
def authorize_callback():
    """Get user token."""

    code = request.args.get('code')
    
    payload = crud.getToken(code)
    if payload:
        session['token'] = payload[0]
        session['refresh_token'] = payload[1]
        session['token_expiration'] = time.time() + payload[2]
    else:
        #error
        print('Token access failed')

    user = crud.getUserInfo(session)
    session['user_id'] = user['id']
    logging.info('new user:' + session['user_id'])
    print(session['user_id'])

    return redirect('/')


@app.route('/playlists')
def getPlaylists(): 
    """Get a list of a user's playlists."""

    playlists = crud.getPlaylists(session)

    return playlists


@app.route('/tracks/<playlist_id>')
def getTracks(playlist_id):
    """Get the tracks in a playlist."""

    tracks = crud.getTracks(session, playlist_id)

    return tracks




if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)