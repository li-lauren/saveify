import unittest
from server import app
import vcr

from urllib.parse import urlparse
import requests
import crud
import os

ACCESS_TOKEN = os.environ['ACCESS_TOKEN']
REFRESH_TOKEN = os.environ['REFRESH_TOKEN']
EXPIRATION = os.environ['EXPIRATION']

class FlaskTests(unittest.TestCase):

    def setUp(self):
        """Work to be done before each test."""

        # Get the Flask test client
        self.client = app.test_client()
        app.config['TESTING'] = True
        app.config['SECRET_KEY'] = 'testkey'
        
        with self.client as c:
            with c.session_transaction() as sess:
                sess['token'] = ACCESS_TOKEN
                sess['refresh_token'] = REFRESH_TOKEN
                sess['token_expiration'] = EXPIRATION

    def tearDown(self):
        """Work to be done after each test."""
        print('Tested')

    # def test_home(self):
    #     """Test for initial home page route."""

    #     result = self.client.get("/")
    #     self.assertEqual(result.status_code, 200)
    #     self.assertIn(b'Saveify', result.data)

    def test_auth(self):
        """Test redirection to Spotify OAuth."""

        # expectedPath = 'https://accounts.spotify.com/authorize?'
        result = self.client.get("/authorize")
        self.assertEqual(result.status_code, 302)
        # self.assertIn(expectedPath, urlparse(result.location).path)

    @vcr.use_cassette('fixtures/vcr_cassettes/google_test.yaml')
    def test_google(self):
        response = requests.get('https://google.com')
        self.assertEqual(response.status_code, 200)

    # @vcr.use_cassette('fixtures/vcr_cassettes/get_playlists_test.yaml')
    def test_get_playlists(self):
        result = self.client.get("/playlists")
        self.assertEqual(result.status_code, 200)
        self.assertIn(b'Discover Weekly', result.data)
        # response = crud.getPlaylists(self.client.session_transaction())
        # self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
