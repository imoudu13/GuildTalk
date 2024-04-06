import unittest
from unittest.mock import patch
from flask import Flask
from inviteToChannel import addUserToChannel


class TestAddUserToChannel(unittest.TestCase):

    @patch('inviteToChannel.db')
    def test_add_user_to_channel_success(self, mock_db):
        # Mock the database handler
        mock_user = {"_id": "123", "channels": []}
        mock_channel_info = {"users": []}
        mock_db.retrieve_document.side_effect = [mock_user, mock_channel_info]
        mock_db.update.side_effect = [True, True]

        # Create a Flask application context
        app_instance = Flask(__name__)
        with app_instance.app_context():
            # Call the function to add a user to a channel
            response = addUserToChannel("test_channel", "test_user")

            # Check if the function returns a success response
            self.assertEqual(response.json, {'success': True})

    @patch('inviteToChannel.db')
    def test_add_user_to_channel_failure_user_not_found(self, mock_db):
        # Mock the database handler
        mock_db.retrieve_document.return_value = None

        # Create a Flask application context
        app_instance = Flask(__name__)
        with app_instance.app_context():
            # Call the function to add a user to a channel with a non-existing user
            response = addUserToChannel("test_channel", "non_existing_user")

            # Check if the function returns a failure response due to user not found
            self.assertEqual(response.json, {'success': False, 'error': 'User not found'})

    @patch('inviteToChannel.db')
    def test_add_user_to_channel_failure_user_already_in_channel(self, mock_db):
        # Mock the database handler
        mock_user = {"_id": "123", "channels": ["test_channel"]}
        mock_channel_info = {"users": ["test_user"]}
        mock_db.retrieve_document.side_effect = [mock_user, mock_channel_info]

        # Create a Flask application context
        app_instance = Flask(__name__)
        with app_instance.app_context():
            # Call the function to add a user to a channel where user is already in the channel
            response = addUserToChannel("test_channel", "test_user")

            # Check if the function returns a failure response due to user already in the channel
            self.assertEqual(response.json, {'success': False, 'error': 'User already in channel'})


if __name__ == '__main__':
    unittest.main()
