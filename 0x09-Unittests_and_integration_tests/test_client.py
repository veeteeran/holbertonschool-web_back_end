#!/usr/bin/env python3
"""Module for client.py unit tests"""
from client import GitHubOrgClient
import json
from parameterized import parameterized
import requests
import unittest
from unittest.mock import patch


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
