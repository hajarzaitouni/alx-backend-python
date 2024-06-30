#!/usr/bin/env python3
""" Unittest module """

import unittest
from unittest.mock import patch, PropertyMock
from client import GithubOrgClient
from parameterized import parameterized


class TestGithubOrgClient(unittest.TestCase):
    """ Test case for GithubOrgClient. """
    @parameterized.expand([
        ("google", ),
        ("abc", ),
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get):
        """ Test org function. """

        mock_get.return_value = {"test": "testing_value"}
        test_client = GithubOrgClient(org_name)
        result = test_client.org
        self.assertEqual(result, {"test": "testing_value"})
        mock_get.assert_called_once_with(
            "https://api.github.com/orgs/"+org_name
            )

    def test_public_repos_url(self):
        """ Test public_repos_url function. """
        with patch.object(GithubOrgClient,
                          "org",
                          new_callable=PropertyMock,
                          return_value={"repos_url": "alx"}) as mock_get:
            test_json = {"repos_url": "alx"}
            test_client = GithubOrgClient(test_json.get("repos_url"))
            test_return = test_client._public_repos_url
            mock_get.assert_called_once
            self.assertEqual(test_return,
                             mock_get.return_value.get("repos_url"))


if __name__ == '__main__':
    unittest.main()
