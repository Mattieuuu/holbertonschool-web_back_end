#!/usr/bin/env python3
"""Unit tests for the github org client module."""

import unittest
from unittest.mock import patch

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


if __name__ == "__main__":
    unittest.main()
