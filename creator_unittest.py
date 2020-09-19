#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import unittest
import creator


class TestFunctions(unittest.TestCase):
    """Test cases.

    Arguments:
        unittest {TestCase} -- unittest
    """

    def setUp(self):
        self.test_class = creator.Creator()

    def test_sample_function_01(self):
        """Test01 for sample_function
        """

        self.assertEqual(self.test_class.camelcase_to_snakcase('ProjectName'), 'project_name')

    def test_sample_function_02(self):
        """Test01 for sample_function
        """

        self.assertEqual(self.test_class.snakecase_to_camelcase('almas_retes'), 'AlmasRetes')

    def test_sample_function_03(self):
        """Test01 for sample_function
        """

        self.assertEqual(self.test_class.create_folder("test"), True)

    def test_sample_function_04(self):
        """Test01 for sample_function
        """

        self.assertEqual(self.test_class.get_home_dir(), "j")


if __name__ == '__main__':
    unittest.main()
