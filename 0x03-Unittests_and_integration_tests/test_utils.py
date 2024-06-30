#!/usr/bin/env python3
""" Unittest module """
import unittest
from parameterized import parameterized
from unittest.mock import patch, Mock
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    """ Unit test class for the access_nested_map function. """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, output):
        """ Test access_nested_map function """
        self.assertEqual(access_nested_map(nested_map, path), output)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b")),
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """ Test that KeyError is raised for invalid paths  """
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """ Unit test class for the get_json function. """

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @patch('utils.requests.get')
    def test_get_json(self, test_url, test_payload, mock_get):
        """ Test get_json function """
        mock_resp = Mock()  # create a mock response
        mock_resp.json.return_value = test_payload
        mock_get.return_value = mock_resp
        self.assertEqual(get_json(test_url), test_payload)


class TestMemoize(unittest.TestCase):
    """ Unit test class for the memoize decorator. """
    def test_memoize(self,):
        """ Test the momoize decorator """
        class TestClass:
            """ nested class """
            def a_method(self):
                """ return a value of 42 """
                return 42

            @memoize
            def a_property(self):
                """ a property """
                return self.a_method()
        with patch.object(TestClass, 'a_method', return_value=42) as mocked:
            test_class = TestClass()

            # Call the memoized property twice
            r1 = test_class.a_property
            r2 = test_class.a_property

            # Assert that a_method was called only once
            mocked.assert_called_once()

            self.assertEqual(r1, 42)
            self.assertEqual(r2, 42)


if __name__ == '__main__':
    unittest.main()
