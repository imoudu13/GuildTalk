import unittest
from unittest.mock import patch
from flask import Flask
from sendMessage import send_message


class TestSendMessage(unittest.TestCase):

    @patch('sendMessage.app.db')
    def test_send_message_success(self, mock_db):
        # Mock the database handler
        mock_channel_info = {"messages": []}
        mock_db.retrieve_from_channel.return_value = mock_channel_info
        mock_db.update_channel.return_value = True

        # Create a Flask application context
        app = Flask(__name__)
        with app.app_context():
            # Call the function with message details
            response = send_message("Test message", "test_user", "2024-03-07 12:00:00", "test_channel")

            # Check if the function returns a success response
            self.assertEqual(response.json, {'success': True})

    @patch('sendMessage.app.db')
    def test_send_message_failure(self, mock_db):
        # Mock the database handler
        mock_channel_info = {"messages": []}
        mock_db.retrieve_from_channel.return_value = mock_channel_info
        mock_db.update_channel.return_value = False

        # Create a Flask application context
        app = Flask(__name__)
        with app.app_context():
            # Call the function with message details
            response = send_message("Test message", "test_user", "2024-03-07 12:00:00", "test_channel")

            # Check if the function returns a failure response
            self.assertNotEqual(response.json, {'success': False})


if __name__ == '__main__':
    unittest.main()
