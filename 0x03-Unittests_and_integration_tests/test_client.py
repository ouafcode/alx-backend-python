#!/usr/bin/env python3
""" tests GithubOrg """
import unittest

from unittest.mock import patch, Mock
from parameterized import parameterized, parameterized_class
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """ tests doc """
    @parameterized.expand([
        ("google"),
        ("abc"),
    ])
    @patch("client.get_json", return_value={"payload": True})
    def test_org(self, org_name: str, mock_get: Mock) -> None:
        """ tests doc """
        get_url = GithubOrgClient(org_name)
        self.assertEqual(get_url.org, {"payload": True})
        url = f"https://api.github.com/orgs/{org_name}"
        mock_get.assert_called_once_with(url)
