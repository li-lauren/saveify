import unittest
import json
from server import app
from model import connect_to_db, example_data, db
import vcr

from urllib.parse import urlparse
import requests
import crud
import os

ACCESS_TOKEN = os.environ['ACCESS_TOKEN']
REFRESH_TOKEN = os.environ['REFRESH_TOKEN']
EXPIRATION = os.environ['EXPIRATION']

my_vcr = vcr.VCR()


class FlaskTests(unittest.TestCase):

    def setUp(self):
        """Work to be done before each test."""

        # Get the Flask test client
        self.client = app.test_client()
        app.config['TESTING'] = True
        app.config['SECRET_KEY'] = 'testkey'

        #Connect to test database
        connect_to_db(app, "postgresql:///testdb")

        #Create tables and add sample data
        db.create_all()
        example_data()
        
        with self.client as c:
            with c.session_transaction() as sess:
                sess['user_id'] = 1
                sess['token'] = ACCESS_TOKEN
                sess['refresh_token'] = REFRESH_TOKEN
                sess['token_expiration'] = EXPIRATION

    def tearDown(self):
        """Work to be done after each test."""
        print('Tested')

    def test_home(self):
        """Test for initial home page route."""

        result = self.client.get("/")
        self.assertEqual(result.status_code, 200)
        self.assertIn(b'Saveify', result.data)

    def test_auth(self):
        """Test redirection to Spotify OAuth."""

        expectedPath = 'https://accounts.spotify.com/authorize?'
        result = self.client.get("/authorize")
        self.assertEqual(result.status_code, 302)
        redirectURL = urlparse(result.location)
        self.assertEqual("/authorize", redirectURL.path)
        self.assertEqual("accounts.spotify.com", redirectURL.hostname)
        self.assertEqual("https", redirectURL.scheme)

    @vcr.use_cassette('fixtures/vcr_cassettes/google_test.yaml')
    def test_google(self):
        """Sample test for vcr.py."""

        response = requests.get('https://google.com')
        self.assertEqual(response.status_code, 200)

    # Define sensitive information
    hidden_headers = [('Authorization', 'XXXX')]
    hidden_params = [('refresh_token', 'XXXX'), ('client_id', 'XXXX'), ('client_secret', 'XXXX')]

    @vcr.use_cassette('fixtures/vcr_cassettes/get_playlists_test.yaml', filter_headers=hidden_headers, filter_post_data_parameters=hidden_params)
    def test_get_playlists(self):
        """Test getting a list of a user's playlists from Spotify API."""

        result = self.client.get("/playlists")

        self.assertEqual(result.status_code, 200)
        self.assertEqual(result.headers.get('Content-Type'), 'application/json')
        data = json.loads(result.data)
        self.assertIn(b'Discover Weekly', result.data)

        # response = crud.getPlaylists(self.client.session_transaction())
        # self.assertEqual(response.status_code, 200)

    @vcr.use_cassette('fixtures/vcr_cassettes/save_playlist_test.yaml', filter_headers=hidden_headers, filter_post_data_parameters=hidden_params)
    def test_save_playlist(self):
        """Test saving a playlist and copying over initial tracks."""

        body = {
            'title':'VCR Test Playlist', 
            'interval':'weekly',
            'playlist_id':'37i9dQZEVXcHh9eQliKRvV'
        }
        result = self.client.post("/save", 
        json=body,
        follow_redirects=True
        )
        self.assertEqual(result.status_code, 200)
        self.assertIn(b'snapshot_id', result.data)



if __name__ == '__main__':
    unittest.main()
