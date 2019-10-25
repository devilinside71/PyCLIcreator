# -*- coding: utf-8 -*-
"""
This module tests for alom_mano.
alom_mano module:

"""
import sys
import unittest
import alom_mano


class testFunctions(unittest.TestCase):
    """Test cases.

    Arguments:
        unittest {TestCase} -- unittest
    """

    def setUp(self):
        self.test_str_01 = 'input text'

    def test_sample_function(self):
        """Test01
        """

        test_class = alom_mano.Alom_Mano()
        test_class.par_input = self.test_str_01
        self.assertEqual(test_class.sample_function(), 'inp text')


if __name__ == '__main__':
    unittest.main()