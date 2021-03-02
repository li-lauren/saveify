import unittest
from server import app

class FlaskTests(unittest.TestCase):

    def setUp(self):
        """Work to be done before each test."""

        # Get the Flask test client
        self.client = app.test_client()
        app.config['TESTING'] = True

    def tearDown(self):
        """Work to be done after each test."""
        print('Tested')

    def test_home_page(self):
        """Test for initial home page route."""

        result = self.client.get("/")
        self.assertEqual(result.status_code, 200)
        self.assertIn(b'Saveify', result.data)


if __name__ == '__main__':
    unittest.main()
