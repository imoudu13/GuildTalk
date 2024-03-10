import unittest
from createChannel import get_channels, add_channel


class TestUserFunctions(unittest.TestCase):

    def test_get_channels_for_existing_user(self):
        # Mock the database handler

        # Test retrieving channels for an existing user
        expected_channels = ["general", "random"]
        actual_channels = get_channels('test_user')
        self.assertEqual(expected_channels, actual_channels)

    def test_get_channels_for_nonexistent_user(self):
        # Test retrieving channels for a nonexistent user
        nonexistent_user = 'nonexistent_user'
        expected_channels = []
        actual_channels = get_channels(nonexistent_user)
        self.assertEqual(expected_channels, actual_channels)


if __name__ == '__main__':
    unittest.main()
