#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    def test_firstindex(self):
        self.assertEqual(max_integer([4, 2, 3]), 4)
        self.assertEqual(max_integer([4, 0, 2, 1, 3]), 4)
        self.assertEqual(max_integer([20, -2, 3]), 20)

    def test_oneElement(self):
        self.assertEqual(max_integer([4]), 4)

    def test_lastindex(self):
        self.assertEqual(max_integer([4, 2, 50]), 50)
        self.assertEqual(max_integer([4, 0, 2, 1, 33]), 33)
        self.assertEqual(max_integer([-2, 13, 30]), 30)

    def test_middle(self):
        self.assertEqual(max_integer([4, 8, 1]), 8)
        self.assertEqual(max_integer([4, 33, 100, 1, 33]), 100)
        self.assertEqual(max_integer([-2, 13, 3]), 13)

    def test_empty(self):
        self.assertEqual(max_integer([]), None)
        string = ""
        self.assertEqual(max_integer(string), None)

    def test_floats(self):
        self.assertEqual(max_integer([4.0, 2.3, 50.20]), 50.20)
        self.assertEqual(max_integer([4.7, 0.6, 2.0, 1, 33.21]), 33.21)
        self.assertEqual(max_integer([-2.5, 13.5, 3.5]), 13.5)

    def test_stringsAndChars(self):
        string = "Hello, World"
        self.assertEqual(max_integer(string), 'r')
        self.assertEqual(max_integer(['A', 'B', 'C', 'D', 'E']), 'E')
        self.assertEqual(max_integer(["Cat", "Banana", "Zebra"]), "Zebra")


if __name__ == '__main__':
    unittest.main()
