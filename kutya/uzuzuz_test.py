# -*- coding: utf-8 -*-
"""
This module tests for uzuzuz.
uzuzuz module:

"""
import sys
import unittest
import uzuzuz


class TestFunctions(unittest.TestCase):
    """Test cases.

    Arguments:
        unittest {TestCase} -- unittest
    """

    def setUp(self):
        self.test_class = uzuzuz.Uzuzuz()

    def test_sample_function_01(self):
        """Test01 for sample_function
        """

        self.assertEqual(self.test_class.sample_function('sample result'), 'sample result')

    def test_sample_function_02(self):
        """Test02 for sample_function
        """

        self.assertEqual(self.test_class.sample_function('sample result2'), 'sample wrong result2')


if __name__ == '__main__':
    unittest.main()
