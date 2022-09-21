#!/usr/bin/python3
"""Unittest of max_integer"""

import unittest

max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    def test_max_integer(self):

        self.assertEqual(max_integer([]), None)

        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

        self.assertEqual(max_integer([1, 2, -5, 4]), 4)

        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

        self.assertEqual(max_integer([44, 30, 45, 43]), 45)

        self.assertEqual(max_integer([50, 1, 2, 50]), 50)

        self.assertEqual(max_integer([0]), 0)

        self.assertEqual(max_integer([None]), None)
