#!/usr/bin/env python3
"""
test_utils module. Unit test for utils.access_nested_map
"""
import unittest
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """Implements unittest.TestCase"""

    @parameterized.expand([
        (nested_map={"a": 1}, path=("a",), 1),
        (nested_map={"a": {"b": 2}}, path=("a",), {"b": 2}),
        (nested_map={"a": {"b": 2}}, path=("a", "b"), 2),
    ])
    def TestAccessNestedMap.test_access_nested_map(self, nested_map,
                                                   path, expected):
        """
        This method test that the method returns what
        it is supposed to"""
        result = access_nested_map(nested_map, path)

        self.assertEqual(result, expected)
