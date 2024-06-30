#!/usr/bin/env python3
""" Unittest module """

import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """ Test case for GithubOrgClient. """

    @parameterized.expand([
        ("google", ),
        ("abc", ),
    ])
    @patch('client.get_json')
    def test_org(self, org, mock_get):
        """ Test GithubOrgClient.org returns the correct value """
        # Set a mock return value
        mock_get.return_value = {"test": "testing_value"}

        test_client = GithubOrgClient(org)
        result = test_client.org
        self.assertEqual(result, {"test": "testing_value"})
        mock_get.assert_called_once_with(f"https://api.github.com/orgs/{org}")


if __name__ == '__main__':
    unittest.main()
