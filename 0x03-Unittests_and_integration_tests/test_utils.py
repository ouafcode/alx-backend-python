#!/usr/bin/env python3
from utils import access_nested_map, get_json, memoize
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
    def test_get_json(self, test_url: str, test_payload: Dict[str, Any],
                      resp_mock: Mock) -> None:
        """ docs test """
        resp_mock.return_value.json.return_value = test_payload
        self.assertEqual(get_json(test_url), test_payload)
        resp_mock.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):
    """ test Memoize """

    def test_memoize(self):
        """ test docs """

        class TestClass:
            """ docs """
            def a_method(self):
                """ docs """
                return 42

            @memoize
            def a_property(self):
                """ docs """
                return self.a_method()

        with patch.object(TestClass, "a_method", return_value=42) as mocked:
            test_class = TestClass()
            self.assertEqual(test_class.a_property, 42)
            self.assertEqual(test_class.a_property, 42)
            mocked.assert_called_once()


if __name__ == '__main__':
    unittest.main()
