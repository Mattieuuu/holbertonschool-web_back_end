#!/usr/bin/env python3
"""Unit tests for the github org client module."""

import unittest
from unittest.mock import patch, PropertyMock, MagicMock

from parameterized import parameterized, parameterized_class

from client import GithubOrgClient
from fixtures import TEST_PAYLOAD


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

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(
        self, repo: dict, license_key: str, expected: bool,
    ) -> None:
        """Test has_license returns expected value for license match."""
        self.assertEqual(
            GithubOrgClient.has_license(repo, license_key),
            expected,
        )


@parameterized_class(
    ("org_payload", "repos_payload", "expected_repos", "apache2_repos"),
    TEST_PAYLOAD,
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration tests for GithubOrgClient using fixtures."""

    @classmethod
    def setUpClass(cls) -> None:
        """Set up mock for requests.get with side_effect."""
        cls.get_patcher = patch("requests.get")
        mock_get = cls.get_patcher.start()

        def side_effect_func(url):
            """Return mock response with json() returning fixture data."""
            mock_response = MagicMock()
            if url == "https://api.github.com/orgs/google":
                mock_response.json.return_value = cls.org_payload
            elif url == cls.org_payload.get("repos_url"):
                mock_response.json.return_value = cls.repos_payload
            return mock_response

        mock_get.side_effect = side_effect_func

    @classmethod
    def tearDownClass(cls) -> None:
        """Stop the patcher."""
        cls.get_patcher.stop()

    def test_public_repos(self) -> None:
        """Test public_repos returns expected list."""
        client = GithubOrgClient("google")
        repos = client.public_repos()
        self.assertEqual(repos, self.expected_repos)

    def test_public_repos_with_apache2_license(self) -> None:
        """Test public_repos with Apache 2.0 license filter."""
        client = GithubOrgClient("google")
        repos = client.public_repos(license="apache-2.0")
        self.assertEqual(repos, self.apache2_repos)


if __name__ == "__main__":
    unittest.main()
