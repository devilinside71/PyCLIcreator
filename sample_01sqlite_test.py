# -*- coding: utf-8 -*-
"""
This module tests for __PROJECTNAMELCASE__.
__PROJECTNAMELCASE__ module:
__DESCRIPTION__
"""
import sys
import unittest
import __PROJECTNAMELCASE__


class TestFunctions(unittest.TestCase):
    """Test cases.

    Arguments:
        unittest {TestCase} -- unittest
    """

    def setUp(self):
        self.test_class = __PROJECTNAMELCASE__.__PROJECTNAME__()

    def test_sample_function_01(self):
        """Test01 for sample_function
        """

        self.assertEqual(self.test_class.sample_function('sample result'), 'sample result')

    def test_sample_function_02(self):
        """Test02 for sample_function
        """

        self.assertEqual(self.test_class.sample_function('sample result2'), 'sample wrong result2')

    def test_gui(self):
        """Test GUI.
        """
        self.test_class.create_gui()

if __name__ == '__main__':
    unittest.main()
