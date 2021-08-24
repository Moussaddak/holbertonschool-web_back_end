#!/usr/bin/env python3
"""
    module of test_utils
"""
import unittest
from utils import access_nested_map, get_json, memoize
from parameterized import parameterized
from typing import Mapping, Sequence, Any
from unittest.mock import patch, Mock


class TestAccessNestedMap(unittest.TestCase):
    """ TestAccessNestedMap Class """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map: Mapping,
                               path: Sequence, expected: Any) -> bool:
        """
            test method access_nested_map
        :param nested_map:
        :param path:
        :param expected:
        :return:
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """
            test method access_nested_map_exception
        :param nested_map:
        :param path:
        :return:
        """
        self.assertRaises(KeyError, access_nested_map, nested_map, path)


class TestGetJson(unittest.TestCase):
    """ TestGetJson class """

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @patch('utils.requests.get')
    def test_get_json(self, url, payload, request):
        """
            test method get_json
        :param url:
        :param expected_payload:
        :param mock_requests:
        :return:
        """

        request.return_value = Mock(ok=True)
        request.return_value.json.return_value = payload

        result = get_json(url)

        self.assertEqual(result, payload)


class TestMemoize(unittest.TestCase):
    """ TestMemoize class """

    def test_memoize(self):
        """ test_memoize class """

        class TestClass:
            """ TestClass class"""

            def a_method(self):
                """ method """
                return 42

            @memoize
            def a_property(self):
                """ property """
                return self.a_method()

        with patch.object(TestClass, 'a_method') as mock:
            test = TestClass()
            test.a_property()
            test.a_property()

            mock.assert_called_once()
