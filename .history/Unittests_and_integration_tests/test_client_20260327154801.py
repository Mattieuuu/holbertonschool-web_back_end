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


if __name__ == "__main__":
    unittest.main()
