import unittest
from DatabaseConnections import DatabaseConnect


class TestDatabaseConnect(unittest.TestCase):

    def setUp(self):
        self.db_connect = DatabaseConnect()

    def test_insert_into_user_successful(self):
        data = ('momo', 'test_password', 'Test', 'User', 'test@example.com')
        result = self.db_connect.insert_into_user(data)
        self.assertTrue(result)

    def test_insert_into_user_failure(self):
        data = ('test_user', 'test_password', 'Test', 'User')  # Missing email
        result = self.db_connect.insert_into_user(data)
        self.assertFalse(result)

    def test_retrieve_from_user_existing_user(self):
        username = 'momo'
        result = self.db_connect.retrieve_from_user(username)
        expected_result = {"username": 'momo', "password": 'test_password', "first": 'Test', "last": 'User',
                           "email": 'test@example.com'}
        self.assertEqual(result, expected_result)

    def test_retrieve_from_user_nonexistent_user(self):
        username = 'nonexistent_user'
        result = self.db_connect.retrieve_from_user(username)
        self.assertIsNone(result)

    def test_retrieve_from_channel_existing_channel(self):
        channel_id = 1
        result = self.db_connect.retrieve_from_channel(channel_id)
        expected_result = {"id": channel_id, "name": "Tech Talk", "creator": "imoudu"}
        self.assertEqual(result, expected_result)

    def test_retrieve_from_channel_nonexistent_channel(self):
        channel_id = 9999
        result = self.db_connect.retrieve_from_channel(channel_id)
        self.assertIsNone(result)

    def test_insert_into_user_channel_successful(self):
        data = ('john_doe', 3, 'FALSE')
        result = self.db_connect.insertIntoUserChannel(data)
        self.assertTrue(result)

    def test_insert_into_message_successful(self):
        data = ('sender_user', 1, "", 'Hello!', '2022-01-01 12:00:00')
        result = self.db_connect.insert_into_message(data)
        self.assertTrue(result)

    def test_insert_into_message_failure_missing_data(self):
        # Simulate a failure by providing incorrect data (missing values)
        data = ('sender_user', 1, "", 'Hello!')  # Missing timeSent
        result = self.db_connect.insert_into_message(data)
        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()
