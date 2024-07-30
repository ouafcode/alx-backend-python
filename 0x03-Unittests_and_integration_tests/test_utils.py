#!/usr/bin/env python3
from utils import access_nested_map
from parameterized import parameterized, parameterized_class


import unittest


class TestAccessNestedMap(unittest.TestCase):
     """ test Access Nested Map """
     @parameterized.expand([
         ({"a": 1}, ("a",), 1),
         ({"a": {"b": 2}}, ("a",), {"b": 2}),
         ({"a": {"b": 2}}, ("a", "b"), 2),
     ])
     def test_access_nested_map(self, nested_map, path, expected):
         """ test result """
         self.assertEqual(access_nested_map(nested_map, path), expected)

if __name__ == '__main__':
    unittest.main()
