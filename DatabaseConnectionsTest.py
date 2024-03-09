import unittest
from datetime import datetime
from DatabaseConnections import DatabaseConnect


class TestDatabaseConnect(unittest.TestCase):

    def setUp(self):
        self.db_connect = DatabaseConnect('GuildTalk')

    def test_insert_into_user_successful(self):
        data = {'_id': 'dude', 'password': 'test_password', 'firstname': 'Test', 'lastname': 'User',
                'email': 'test@example.com'}
        result = self.db_connect.insert_into_user(data)
        self.assertTrue(result)

    def test_insert_into_user_failure(self):
        data = {'_id': 'test_user', 'password': 'test_password', 'firstname': 'Test',
                'lastname': 'User'}  # Missing email
        result = self.db_connect.insert_into_user(data)
        self.assertFalse(result)

    def test_retrieve_from_user_existing_user(self):
        username = 'dude'
        result = self.db_connect.retrieve_from_user(username)
        expected_result = {"_id": 'dude', "password": 'test_password', "first": 'Test', "last": 'User',
                           "email": 'test@example.com'}
        self.assertEqual(result, expected_result)

    def test_retrieve_from_user_nonexistent_user(self):
        username = 'nonexistent_user'
        result = self.db_connect.retrieve_from_user(username)
        self.assertIsNone(result)

    def test_insert_into_channel_successful(self):
        data = {'_id': 1, 'name': 'New Channel', 'creator': 'john_doe'}
        result = self.db_connect.insert_into_channel(data)
        self.assertTrue(result)

    def test_retrieve_from_channel_existing_channel(self):
        channel_id = 1
        result = self.db_connect.retrieve_from_channel(channel_id)
        expected_result = {"_id": channel_id, "name": "'New Channel", "creator": "john_doe"}
        self.assertEqual(result, expected_result)

    def test_retrieve_from_channel_nonexistent_channel(self):
        channel_id = 9999
        result = self.db_connect.retrieve_from_channel(channel_id)
        self.assertIsNone(result)

    def test_insert_into_user_channel_successful(self):
        data = {'_id': 'john_doe', 'ChannelID': 3, 'IsAdmin': False}
        result = self.db_connect.insert_into_user_channel(data)
        self.assertTrue(result)

    def test_insert_into_message_successful(self):
        data = {'senderUsername': 'sender_user', 'channelID': 1, 'receiverUsername': '', 'content': 'Hello!',
                'timeSent': datetime.now()}
        result = self.db_connect.insert_into_message(data)
        self.assertTrue(result)

    def test_insert_into_message_failure_missing_data(self):
        # Simulate a failure by providing incorrect data (missing values)
        data = {'senderUsername': 'sender_user', 'channelID': 1, 'content': 'Hello!'}  # Missing timeSent
        result = self.db_connect.insert_into_message(data)
        self.assertFalse(result)

    def test_update_user_success(self):
        data = information = {'username': 'haha', 'firstname': 'Imoudu', 'lastname': 'Ibrahim',
                              'email': 'imoudu@gmail.com', 'password': 'guildtalk24'}
        result = self.db_connect.update_user(data)
        self.assertTrue(result)

    def test_update_user_failure(self):
        data = information = {'username': 'imoudu', 'firstname': 'Imoudu', 'lastname': 'Ibrahim',
                              'email': 'imoudu@gmail.com', 'password': 'guildtalk24'}  # missing original username
        result = self.db_connect.update_user(data)
        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()
