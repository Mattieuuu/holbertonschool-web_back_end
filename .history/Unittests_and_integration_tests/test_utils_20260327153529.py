#!/usr/bin/env python3
"""Unit tests for utility helpers."""

import unittest
from typing import Any, Mapping, Sequence
from unittest.mock import Mock, patch

from parameterized import parameterized

from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    """Tests for the access_nested_map function."""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(
        self,
        nested_map: Mapping[str, Any],
        path: Sequence[str],
        expected: Any,
    ) -> None:
        """Check that nested values are correctly returned."""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b")),
    ])
    def test_access_nested_map_exception(
        self,
        nested_map: Mapping[str, Any],
        path: Sequence[str],
    ) -> None:
        """Check that missing keys raise the expected KeyError."""
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)

        self.assertEqual(str(context.exception), repr(path[-1]))


class TestGetJson(unittest.TestCase):
    """Tests for the get_json function."""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(
        self,
        test_url: str,
        test_payload: Mapping[str, bool],
    ) -> None:
        """Check that get_json returns expected payload from mocked call."""
        with patch("utils.requests.get") as mock_get:
            mock_response = Mock()
            mock_response.json.return_value = test_payload
            mock_get.return_value = mock_response

            self.assertEqual(get_json(test_url), test_payload)
            mock_get.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):
    """Tests for the memoize decorator."""

    def test_memoize(self) -> None:
        """Check that memoized property calls underlying method once."""

        class TestClass:
            """Simple class used for memoization testing."""

            def a_method(self) -> int:
                """Return a constant value."""
                return 42

            @memoize
            def a_property(self) -> int:
                """Memoized property calling a_method."""
                return self.a_method()

        with patch.object(
            TestClass, "a_method", return_value=42,
        ) as mock_method:
            test_object = TestClass()
            self.assertEqual(test_object.a_property(), 42)
            self.assertEqual(test_object.a_property(), 42)
            mock_method.assert_called_once()


if __name__ == "__main__":
    unittest.main()
