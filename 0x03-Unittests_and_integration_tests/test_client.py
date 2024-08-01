#!/usr/bin/env python3
""" tests GithubOrg """
import unittest

from unittest.mock import patch, Mock, PropertyMock
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

    @patch("client.GithubOrgClient.org", new_callable=PropertyMock)
    def test_public_repos_url(self, mock_org) -> None:
        """doc doc doc"""
        payload = {"repos_url": "https://api.github.com/orgs/google/repos"}
        mock_org.return_value = payload
        github_org_client = GithubOrgClient("google")
        self.assertEqual(github_org_client._public_repos_url,
                         payload["repos_url"])

    @patch("client.get_json", return_value=[{"name": "repos1"},
                                            {"name": "repos2"}])
    def test_public_repos(self, mock_get: Mock) -> None:
        """ doc doc test """
        with patch("client.GithubOrgClient._public_repos_url",
                   new_callable=PropertyMock) as mock_public:
            mock_public.return_value = (
                    "https://api.github.com/orgs/google/repos"
            )
            github_url = GithubOrgClient("google")
            self.assertEqual(github_url.public_repos(), ["repos1", "repos2"])
            mock_get.assert_called_once()
            mock_public.assert_called_once()

    @parameterized.expand(
        [
            ({"license": {"key": "my_license"}}, "my_license", True),
            ({"license": {"key": "other_license"}}, "my_license", False),
        ]
    )
    def test_has_license(self, repos, licence_key, expected):
        """ doc doc tests """
        github_org = GithubOrgClient("google")
        self.assertEqual(
                github_org.has_license(repos, licence_key), expected
        )
