#!/usr/bin/env python3
"""Module for client.py unit tests"""
from client import GitHubOrgClient
from fixtures import TEST_PAYLOAD
import json
from parameterized import parameterized, parameterized_class
import requests
import unittest
from unittest.mock import patch, PropertyMock


class TestGitHubOrgClient(unittest.TestCase):
    """GitHubOrgClient unit tests"""
    @parameterized.expand([
        'google',
        'abc'
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        """Test that GitHubOrgClient.org returns the correct value"""
        test_obj = GitHubOrgClient(org_name)
        url = f"https://api.github.com/orgs/{org_name}"
        test_obj.org()
        mock_get_json.assert_called_once_with(url)

    def test_public_repos_url(self):
        """Test that the result of _public_repos_url is the expected one based
        on the mocked payload"""
        '''
        with patch.object(GitHubOrgClient, 'org') as mock_org:
            test_obj = GitHubOrgClient('google')
            payload = "https://api.github.com/orgs/google/repos"
            p = PropertyMock(return_value=payload)
            GitHubOrgClient._public_repos_url = p
            self.assertEqual(test_obj._public_repos_url, payload)
        '''
        with patch('client.GitHubOrgClient.org',
                   new_callable=PropertyMock) as mock_org:
            mock_org.return_value = "https://api.github.com/orgs/google/repos"
            myClass = GitHubOrgClient('google')
            p = PropertyMock(return_value=mock_org.return_value)
            GitHubOrgClient._public_repos_url = p
            self.assertEqual(myClass._public_repos_url, mock_org.return_value)

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        """public_repos unit test
        - list of repos is what you expect from the chosen payload
        - mocked property and the mocked get_json was called once"""
        with patch('client.GitHubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as mock_public_repos_url:

            payload = {'login': 'microsoft',
                       'id': 6154722,
                       'node_id': 'MDEyOk9yZ2FuaXphdGlvbjYxNTQ3MjI=',
                       'url': 'https://api.github.com/orgs/microsoft',
                       'repos_url':
                       'https://api.github.com/orgs/microsoft/repos'}

            test_object = GitHubOrgClient('foo')
            mock_get_json.return_value = payload
            org = test_object.org
            mock_public_repos_url.return_value = org.get('repos_url')

            self.assertEqual(test_object._public_repos_url,
                             'https://api.github.com/orgs/microsoft/repos')
            mock_get_json.assert_called_once()
            mock_public_repos_url.assert_called_once_with()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(self, repo, license_key, expected):
        """has_license unit-test"""
        test_object = GitHubOrgClient('foo')
        self.assertEqual(test_object.has_license(repo, license_key), expected)

        with self.assertRaises(AssertionError):
            test_object.has_license(repo, None)


'''
mock get_json since public_repos calls repos_payload which calls get_json
'''
'''
@parameterized_class("org_payload", "repos_payload", "expected_repos",
                     "apache2_repos")
class TestIntegrationGitHubOrgClient(unittest.TestCase):
    """GitHubOrgClient.public_repos integration tests"""
    def get_names():
        """get names from fixtures.py"""
        names = [data.get("name") for data in TEST_PAYLOAD[0][1]]
        return names

    @classmethod
    def setUpClass(cls):
        """mock request.get to return example payloads found in the fixtures"""
        with patch('requests.get') as get_patcher:
            get_patcher.side_effect = TEST_PAYLOAD

    @classmethod
    def tearDownClass(cls):
        """Stops the patcher"""
        pass
'''
