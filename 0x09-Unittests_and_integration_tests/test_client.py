#!/usr/bin/env python3
"""Module for client.py unit tests"""
from client import GitHubOrgClient
import json
from parameterized import parameterized
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
        arg = test_obj.ORG_URL.format(org=org_name)
        url = f"https://api.github.com/orgs/{org_name}"
        self.assertEqual(arg, url)
        test_obj.org
        mock_get_json.assert_called_once()

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
