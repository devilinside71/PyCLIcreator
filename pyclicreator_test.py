# -*- coding: utf-8 -*-
# pylint: disable=C0111
"""
This module tests for pyclicreator.
pyclicreator module:
This class module is...
"""
import sys
import unittest
import pyclicreator


class TestFunctions(unittest.TestCase):
    """Test cases.

    Arguments:
        unittest {TestCase} -- unittest
    """

    def setUp(self):
        self.test_class = pyclicreator.PyCLIcreator()

    def test_get_normalized_name1(self):
        self.assertEqual(self.test_class.get_normalized_name(
            'Árvíztűrő tükörfúrógép', 'normal'), 'Arvizturo tukorfurogep')

    def test_get_normalized_name2(self):
        self.assertEqual(self.test_class.get_normalized_name(
            'Árvíztűrő tükörfúrógép', 'filename'), 'arvizturo_tukorfurogep')

    def test_get_normalized_name3(self):
        self.assertEqual(self.test_class.get_normalized_name(
            'Árvíztűrő tükörfúrógép', 'classname'), 'Arvizturo_Tukorfurogep')

    def test_create_arg_line1(self):
        self.assertEqual(self.test_class.create_arg_line(
            'i', 'input', 'some text', True),
            'parser.add_argument(\'-i\', \'--input\', action=\'store_true\', help=\'some text\')')

    def test_create_arg_line2(self):
        self.assertEqual(self.test_class.create_arg_line(
            'i', 'input', 'some text', False),
            'parser.add_argument(\'-i\', \'--input\', help=\'some text\')')

    def test_create_exec_arg_line(self):
        self.assertEqual(self.test_class.create_exec_arg_line('input'),
                         'if args.input is not None:\n            self.par_input = args.input')

    def test_create_execlog_arg_line(self):
        self.assertEqual(
            self.test_class.create_execlog_arg_line('some text', 'input'),
            'LOGGER.debug(\'some text: %s\', self.par_input)')

    def test_create_init_arg_line(self):
        self.assertEqual(self.test_class.create_init_arg_line(
            'input'), 'self.par_input = \'\'')


if __name__ == '__main__':
    unittest.main()
