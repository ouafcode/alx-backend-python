#!/usr/bin/env python3
from utils import access_nested_map, get_json
from parameterized import parameterized, parameterized_class
from unittest.mock import Mock, patch
from typing import Any, Dict

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

     @parameterized.expand([
         ({}, ("a",)),
         ({"a": 1}, ("a", "b")),
     ])
     def test_access_nested_map_exception(self, nested_map, path):
         """ test exception """
         with self.assertRaises(Exception):
              access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """ test get json """

    @parameterized.expand(
        [
            ("http://example.com", {"payload": True}),
            ("http://holberton.io", {"payload": False}),
        ]
    )
    @patch("requests.get")
    def test_get_json(self, test_url: str, test_payload: Dict[str, Any], resp_mock: Mock) -> None:
        """ docs test """
        resp_mock.return_value.json.return_value = test_payload
        self.assertEqual(get_json(test_url), test_payload)
        resp_mock.assert_called_once_with(test_url)



if __name__ == '__main__':
    unittest.main()
