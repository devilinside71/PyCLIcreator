# -*- coding: utf-8 -*-
# pylint: disable=C0111
"""
This module tests for pyclicreator.
pyclicreator module:
"""

import unittest
import pyclicreator
import textformatter
from textformatter import FormatType


class TestFunctions(unittest.TestCase):
    """Test cases.

    Arguments:
        unittest {TestCase} -- unittest
    """

    def setUp(self):
        self.test_class = pyclicreator.PyCLIcreator()
        self.test_formatter_class = textformatter.TextFormatter()
        self.format_types = FormatType()

    def test_get_normalized_name1(self):
        self.assertEqual(self.test_formatter_class.get_normalized_name(
            'Árvíztűrő tükörfúrógép', self.format_types.NORMAL), 'Arvizturo tukorfurogep')

    def test_get_normalized_name2(self):
        self.assertEqual(self.test_formatter_class.get_normalized_name(
            'Árvíztűrő tükörfúrógép', self.format_types.FILENAME), 'arvizturo_tukorfurogep')

    def test_get_normalized_name3(self):
        self.assertEqual(self.test_formatter_class.get_normalized_name(
            'Árvíztűrő tükörfúrógép', self.format_types.CLASSNAME), 'Arvizturo_Tukorfurogep')

    def test_create_arg_line1(self):
        self.assertEqual(
            self.test_class.create_arg_line(
                'i', 'input', 'some text', True),
            'parser.add_argument(\'-i\', \'--input\', action=\'store_true\', help=\'some text\')')

    def test_create_arg_line2(self):
        self.assertEqual(
            self.test_class.create_arg_line(
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

    def test_arg_valid_1(self):
        self.assertEqual(self.test_class.arg_valid(
            'i', 'input', 'help'), True)

    def test_arg_valid_2(self):
        self.assertEqual(self.test_class.arg_valid(
            'i', 'input', ''), False)


if __name__ == '__main__':
    unittest.main()
