#!/usr/bin/env python3
"""Module for client.py unit tests"""
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD
import json
from parameterized import parameterized, parameterized_class
import requests
import unittest
from unittest.mock import patch, PropertyMock


class TestGithubOrgClient(unittest.TestCase):
    """GitHubOrgClient unit tests"""
    @parameterized.expand([
        'google',
        'abc'
    ])
    @patch('client.get_json', return_value={'key': 'value'})
    def test_org(self, org_name, mock_get_json):
        """Test that GitHubOrgClient.org returns the correct value"""
        test_obj = GithubOrgClient(org_name)
        url = f"https://api.github.com/orgs/{org_name}"

        self.assertEqual(test_obj.org, {'key': 'value'})
        mock_get_json.assert_called_once_with(url)
