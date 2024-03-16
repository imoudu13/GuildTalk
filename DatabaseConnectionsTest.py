import unittest
from DatabaseConnections import DatabaseConnect


class TestDatabaseConnect(unittest.TestCase):

    def setUp(self):
        self.db_connect = DatabaseConnect()

    def test_insert_into_user(self):
        user_data = {
            "_id": "test_user",
            "firstname": "John",
            "lastname": "Doe",
            "email": "john.doe@example.com",
            "password": "password123",
            "channels": ["general"]
        }
        result = self.db_connect.insert_into_user(user_data)
        self.assertTrue(result)

    def test_retrieve_from_user(self):
        username = "test_user"
        result = self.db_connect.retrieve_from_user(username)
        self.assertIsNotNone(result)
        self.assertEqual(result["_id"], username)

    def test_update_user(self):
        user_info = {
            "_id": "test_user",
            "firstname": "UpdatedJohn",
            "lastname": "UpdatedDoe",
            "email": "updated.john.doe@example.com",
            "password": "updated_password123",
            "channels": ["general", "random"]
        }
        result = self.db_connect.update_user(user_info)
        self.assertTrue(result)

    def test_insert_into_channel(self):
        channel_info = {
            "_id": "test_channel",
            "creator": "test_user"
        }
        result = self.db_connect.insert_into_channel(channel_info)
        self.assertTrue(result)

    def test_retrieve_from_channel(self):
        channel_name = "test_channel"
        result = self.db_connect.retrieve_from_channel(channel_name)
        self.assertIsNotNone(result)
        self.assertEqual(result["_id"], channel_name)

    def test_update_channel(self):
        channel_name = "test_channel"
        update_data = {"admins": ["test_user", "admin2"]}
        result = self.db_connect.update_channel(channel_name, update_data)
        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()
