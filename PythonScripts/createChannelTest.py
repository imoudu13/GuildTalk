import unittest
from unittest.mock import patch
from flask import Flask, jsonify
from createChannel import add_channel, get_channels

class TestAddChannel(unittest.TestCase):
    @patch('createChannel.app.db')
    def test_add_channel_success(self, mock_db):
        # Mock the database handler
        mock_user = {"username": "test_user", "channels": []}
        mock_db.retrieve_from_user.return_value = mock_user
        mock_db.insert_into_channel.return_value = True
        mock_db.update_user.return_value = True

        # Create a Flask application context
        app = Flask(__name__)
        with app.app_context():
            # Call the function with a channel name
            response = add_channel('channel_name')

            # Check if the function returns a success response
            self.assertEqual(response.json, {'success': True})

    @patch('createChannel.app.db')
    def test_add_channel_failure(self, mock_db):
        # Mock the database handler
        mock_user = {"username": "test_user", "channels": []}
        mock_db.retrieve_from_user.return_value = mock_user
        mock_db.insert_into_channel.return_value = False
        mock_db.update_user.return_value = True

        # Create a Flask application context
        app = Flask(__name__)
        with app.app_context():
            # Call the function with a channel name
            response = add_channel('channel_name')

            # Check if the function returns a failure response
            self.assertNotEqual(response.json, {'success': False})

    def test_get_channels_for_existing_user(self):
        # Mock the database handler

        # Test retrieving channels for an existing user
        expected_channels = ["general", "random", "jeff", "Hip Hop"]
        actual_channels = get_channels('test_user')
        self.assertEqual(expected_channels, actual_channels)

    def test_get_channels_for_nonexistent_user(self):
        # Test retrieving channels for a nonexistent user
        nonexistent_user = 'nonexistent_user'
        expected_channels = []
        actual_channels = get_channels(nonexistent_user)
        self.assertEqual(expected_channels, actual_channels)

if __name__ == '__main__':
    unittest.main()
