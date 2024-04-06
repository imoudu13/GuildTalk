import unittest
from unittest.mock import patch
from flask import Flask
from deleteMessage import deleteMessage


class TestDeleteMessage(unittest.TestCase):
    @patch('deleteMessage.app.db')
    def test_delete_message_success(self, mock_db):
        # Mock the database handler
        mock_channel_info = {"messages": ["Message 1", "Message 2", "Message 3"]}
        mock_db.retrieve_from_channel.return_value = mock_channel_info
        mock_db.update_channel.return_value = True

        # Create a Flask application context
        app_instance = Flask(__name__)
        with app_instance.app_context():
            # Call the function to delete a message
            response = deleteMessage(1, "Bio 123")

            # Check if the function returns a success response
            self.assertEqual(response.json, {'success': True})

    @patch('deleteMessage.app.db')
    def test_delete_message_failure(self, mock_db):
        # Mock the database handler
        mock_channel_info = {"messages": ["Message 1", "Message 2", "Message 3"]}
        mock_db.retrieve_from_channel.return_value = mock_channel_info
        mock_db.update_channel.return_value = False

        # Create a Flask application context
        app_instance = Flask(__name__)
        with app_instance.app_context():
            # Call the function to delete a message with an invalid index
            response = deleteMessage(-1, "test_channel")

            # Check if the function returns a failure response
            self.assertEqual(response.json, {'success': False, 'error': 'Invalid message index'})


if __name__ == '__main__':
    unittest.main()
