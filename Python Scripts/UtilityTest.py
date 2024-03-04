import unittest
from Utility import insert_into_User, retrieve_from_user


class TestUserFunctions(unittest.TestCase):

    def test_insert_into_User_successful(self):
        data = ('momo', 'test_password', 'Test', 'User', 'test@example.com')
        result = insert_into_User(data)
        self.assertTrue(result)

    def test_insert_into_User_failure(self):
        # Simulate a failure by providing incorrect data (missing values)
        data = ('test_user', 'test_password', 'Test', 'User')  # Missing email
        result = insert_into_User(data)
        self.assertFalse(result)

    def test_retrieve_from_user_nonexistent_user(self):
        # Ensure that the function returns a default value for a non-existing user
        username = 'nonexistent_user'
        result = retrieve_from_user(username)
        self.assertEqual(result, ' ')
