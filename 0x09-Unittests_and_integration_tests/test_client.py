#!/usr/bin/env python3
""" Module for testing client """

from client import GithubOrgClient
from parameterized import parameterized

import unittest
from unittest.mock import patch


class TestGithubOrgClient(unittest.TestCase):
    """ Github org Testing class """

    @parameterized.expand([
        'google',
        'abc'
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock):
        """ method test_org """
        test = GithubOrgClient(org_name)
        mock.side_effect = Exception()
        try:
            test.org()
        except Exception as e:
            mock.assert_called_once_with(
                f'https://api.github.com/orgs/{org_name}')
