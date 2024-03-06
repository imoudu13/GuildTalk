import unittest
import DatabaseConnections


class TestUserFunctions(unittest.TestCase):

    def test_insert_into_User_successful(self):
        data = ('momo', 'test_password', 'Test', 'User', 'test@example.com')
        result = DatabaseConnections.insertIntoUser(data)
        self.assertTrue(result)


