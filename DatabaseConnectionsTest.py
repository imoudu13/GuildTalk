import unittest
import DatabaseConnections


class TestUserFunctions(unittest.TestCase):

    def test_insert_into_User_successful(self):
        data = ('momo', 'test_password', 'Test', 'User', 'test@example.com')
        result = DatabaseConnections.insertIntoUser(data)
        self.assertTrue(result)

    def test_insert_into_User_failure(self):
        # Simulate a failure by providing incorrect data (missing values)
        data = ('test_user', 'test_password', 'Test', 'User')  # Missing email
        result = DatabaseConnections.insertIntoUser(data)
        self.assertFalse(result)

    def test_retrieve_from_user_success(self):
        username = 'momo'
        result = DatabaseConnections.retrieveFromUser(username)
        self.assertEqual(result, {"username": 'momo', "password": 'test_password', "first": 'Test', "last": 'User', "email": 'test@example.com'})

    def test_retrieve_from_user_nonexistent_user(self):
        # Ensure that the function returns a default value for a non-existing user
        username = 'nonexistent_user'
        result = DatabaseConnections.retrieveFromUser(username)
        self.assertEqual(result, None)

    def test_retrieve_from_channel_success(self):
        channel_id = 1  # Assuming a valid channel ID
        result = DatabaseConnections.retrieveFromChannel(channel_id)
        expected_result = {"id": channel_id, "name": "Tech Talk", "creator": "imoudu"}
        self.assertEqual(result, expected_result)

    def test_retrieve_from_channel_nonexistent_channel(self):
        channel_id = 9999  # Assuming an invalid channel ID
        result = DatabaseConnections.retrieveFromChannel(channel_id)
        self.assertIsNone(result)

    def test_insert_into_channel_successful(self):
        data = ('NewChannel', 'test_user')  # Assuming valid channel information
        result = DatabaseConnections.insertIntoChannel(data)
        self.assertTrue(result)

    def test_insert_into_channel_failure(self):
        # Simulate a failure by providing incorrect data (missing values)
        data = ('NewChannel',)  # Missing creator username
        result = DatabaseConnections.insertIntoChannel(data)
        self.assertFalse(result)

    def test_retrieve_message_success(self):
        username = 'john_doe'  # Assuming a valid channel ID with messages
        result = DatabaseConnections.retrieveMessage(username)
        expected_result = {"channel_id": 1, "message_id": 1, "sender": "john_doe", "content": "Hey, how is everyone doing?",
                           'time': '2024-03-03 09:15:00'}
        self.assertEqual(result[0], expected_result)

    def test_retrieve_message_nonexistent_channel(self):
        channel_id = 9999  # Assuming an invalid channel ID
        result = DatabaseConnections.retrieveMessage(channel_id)
        self.assertIsNone(result)

    def test_insert_into_message_successful(self):
        data = ('test_user', 1, 'receiver_user', 'Hello!', '2022-01-01 12:00:00')  # Assuming valid message information
        result = DatabaseConnections.insertIntoMessage(data)
        self.assertTrue(result)

    def test_insert_into_message_failure(self):
        # Simulate a failure by providing incorrect data (missing values)
        data = ('test_user', 1, 'receiver_user', 'Hello!')  # Missing timeSent
        result = DatabaseConnections.insertIntoMessage(data)
        self.assertFalse(result)

    def insert_into_User_Channel(self):
        data = ('john_doe', 3, 'FALSE')
        result = DatabaseConnections.insertIntoUserChannel(data)
        self.assertTrue(result)
