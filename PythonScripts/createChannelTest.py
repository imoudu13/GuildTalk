import unittest
from unittest.mock import patch
from createChannel import get_channels, add_channel


class TestUserFunctions(unittest.TestCase):
    @patch('app.db')
    def test_get_channels_for_existing_user(self, mock_db):
        # Mock the database handler
        mock_db.retrieve_from_user_channel.return_value = [{"channelName": 'Tech Talk', "id": 1}]

        # Test retrieving channels for an existing user
        expected_channels = [{"channelName": 'Tech Talk', "id": 1}]
        actual_channels = get_channels('john_doe')
        self.assertEqual(expected_channels, actual_channels)

    @patch('app.db')
    def test_get_channels_for_nonexistent_user(self, mock_db):
        # Mock the database handler
        mock_db.retrieve_from_user_channel.return_value = []

        # Test retrieving channels for a nonexistent user
        nonexistent_user = 'nonexistent_user'
        expected_channels = []
        actual_channels = get_channels(nonexistent_user)
        self.assertEqual(expected_channels, actual_channels)


if __name__ == '__main__':
    unittest.main()
