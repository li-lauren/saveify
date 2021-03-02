import unittest
from server import app
import vcr

from urllib.parse import urlparse
import requests
import crud

class FlaskTests(unittest.TestCase):

    def setUp(self):
        """Work to be done before each test."""

        # Get the Flask test client
        self.client = app.test_client()
        app.config['TESTING'] = True

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

        # expectedPath = 'https://accounts.spotify.com/authorize?'
        result = self.client.get("/authorize")
        self.assertEqual(result.status_code, 302)
        # self.assertIn(expectedPath, urlparse(result.location).path)

    @vcr.use_cassette('fixtures/vcr_cassettes/google_test.yaml')
    def test_google(self):
        response = requests.get('https://google.com')
        self.assertEqual(response.status_code, 200)
    


if __name__ == '__main__':
    unittest.main()
