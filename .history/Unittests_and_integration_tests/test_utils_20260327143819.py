#!/usr/bin/env python3
"""Unit tests for utility helpers."""

import unittest
from typing import Any, Mapping, Sequence

from parameterized import parameterized

from utils import access_nested_map


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


if __name__ == "__main__":
    unittest.main()