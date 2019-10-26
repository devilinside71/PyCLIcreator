# -*- coding: utf-8 -*-
"""
This module tests for alom_mano.
alom_mano module:

"""
import sys
import unittest
import alom_mano


class TestFunctions(unittest.TestCase):
    """Test cases.

    Arguments:
        unittest {TestCase} -- unittest
    """

    def setUp(self):
        self.test_class = alom_mano.Alom_Mano()

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
