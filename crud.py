"""CRUD operations."""

from model import db, connect_to_db

import os
import base64
import requests
import logging

SPOTIFY_CLIENT_ID = os.environ['SPOTIFY_CLIENT_ID']
SPOTIFY_SECRET = os.environ['SPOTIFY_SECRET']

def getToken(code): 
    token_url = 'https://accounts.spotify.com/api/token'
    authorization = 'Basic ' + base64.standard_b64encode(
        SPOTIFY_CLIENT_ID + ':' + SPOTIFY_SECRET)
    redirect_uri = 'http://0.0.0.0:5000/callback'

    headers = {'Authorization': authorization, 
             'Accept': 'application/json', 
             'Content-Type': 'application/x-www-form-urlencoded'}
    body = {'code': code, 'redirect_uri': redirect_uri, 
            'grant_type': 'authorization_code'}
    post_response = requests.post(token_url,headers=headers,data=body)
    
    if post_response.status_code == 200:
        pr = post_response.json()
        return pr['access_token'], pr['refresh_token'], pr['expires_in']
    else:
        logging.error('getToken:' + str(post_response.status_code))
        return None
    

def refreshToken(refresh_token):
    token_url = 'https://accounts.spotify.com/api/token'
    authorization = 'Basic ' + base64.standard_b64encode(
        SPOTIFY_CLIENT_ID + ':' + SPOTIFY_SECRET)

    headers = {'Authorization': authorization, 'Accept': 'application/json', 'Content-Type': 'application/x-www-form-urlencoded'}
	body = {'refresh_token': refresh_token, 'grant_type': 'refresh_token'}
	post_response = requests.post(token_url, headers=headers, data=body)

	# 200 code indicates access token was properly granted
	if post_response.status_code == 200:
		return post_response.json()['access_token'], post_response.json()['expires_in']
	else:
		logging.error('refreshToken:' + str(post_response.status_code))
		return None


if __name__ == '__main__':
    from server import app
    connect_to_db(app)