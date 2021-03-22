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
        self.test_class = __PROJECTNAMELCASE__.__PROJECTNAME__(True)

    def test_program_01(self):
        """Testing the main program.
        """
        # __UNITTESTARG1__
        # __UNITTESTARG2__
        # __UNITTESTARG3__
        # __UNITTESTARG4__
        # __UNITTESTARG5__
        self.test_class.verbose = True
        self.test_class.execute_program()

    def test_sample_function_01(self):
        """Test01 for sample_function
        """
        input_str = ''
        self.assertEqual(self.test_class.sample_function(
            input_str), 'result')

    def test_sample_function_02(self):
        """Test02 for sample_function
        """
        input_str = ''
        self.assertEqual(self.test_class.sample_function(
            input_str), 'wrong_result2')


if __name__ == '__main__':
    unittest.main()
