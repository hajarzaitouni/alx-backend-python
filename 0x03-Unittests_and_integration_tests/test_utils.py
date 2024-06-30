#!/usr/bin/env python3
""" Unittest module """
import unittest
from parameterized import parameterized
from utils import access_nested_map


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


if __name__ == '__main__':
    unittest.main()