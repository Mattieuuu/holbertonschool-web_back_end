#!/usr/bin/env python3
"""Unit tests for the github org client module."""

import unittest
from unittest.mock import patch, PropertyMock

from parameterized import parameterized

from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Tests for GithubOrgClient."""

    @parameterized.expand([
        ("google", {"login": "google"}),
        ("abc", {"login": "abc"}),
    ])
    @patch("client.get_json")
    def test_org(self, org: str, expected: dict, mock_get_json) -> None:
        """Test org returns payload and calls get_json once."""
        mock_get_json.return_value = expected

        self.assertEqual(GithubOrgClient(org).org, expected)
        mock_get_json.assert_called_once_with(
            "https://api.github.com/orgs/{}".format(org)
        )

    def test_public_repos_url(self) -> None:
        """Test _public_repos_url returns expected url from org payload."""
        expected_url = "https://api.github.com/orgs/google/repos"
        payload = {"repos_url": expected_url}

        with patch.object(
            GithubOrgClient,
            "org",
            new_callable=PropertyMock,
            return_value=payload,
        ):
            self.assertEqual(
                GithubOrgClient("google")._public_repos_url,
                expected_url,
            )

    @patch("client.get_json")
    def test_public_repos(self, mock_get_json) -> None:
        """Test public_repos returns expected names from mocked payload."""
        expected_url = "https://api.github.com/orgs/hbtn/repos"
        payload = [
            {"name": "repo_one"},
            {"name": "repo_two"},
        ]
        expected_repos = ["repo_one", "repo_two"]
        mock_get_json.return_value = payload

        with patch.object(
            GithubOrgClient,
            "_public_repos_url",
            new_callable=PropertyMock,
            return_value=expected_url,
        ) as mock_public_repos_url:
            self.assertEqual(
                GithubOrgClient("google").public_repos(),
                expected_repos,
            )
            mock_public_repos_url.assert_called_once()

        mock_get_json.assert_called_once_with(expected_url)


if __name__ == "__main__":
    unittest.main()
