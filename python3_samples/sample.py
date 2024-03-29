#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
__DESCRIPTION__
"""

import argparse
import errno
import logging
import os
import sys

__author__ = '__AUTHOR__'
__copyright__ = '__COPYRIGHT__, __AUTHOR__'
__license__ = '__LICENCE__'
__version__ = '__VERSION__'
__maintainer__ = '__AUTHOR__'
__email__ = '__EMAIL__'
__status__ = '__STATUS__'


# LOGGER = logging.getLogger('PROJECT_NAME')
# set level for file handling (NOTSET>DEBUG>INFO>WARNING>ERROR>CRITICAL)
# LOGGER.setLevel(logging.DEBUG)

# create file handler which logs even debug messages
# LOGGER_FH = logging.FileHandler('PROJECT_SNAKE.log')

# create console handler with a higher log level
# LOGGER_CH = logging.StreamHandler()
# LOGGER_CH.setLevel(logging.INFO)

# create FORMATTER and add it to the handlers
# FORMATTER = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# LOGGER_FH.setFormatter(FORMATTER)
# LOGGER_CH.setFormatter(FORMATTER)

# add the handlers to the LOGGER
# LOGGER.addHandler(LOGGER_FH)
# LOGGER.addHandler(LOGGER_CH)


class PROJECT_NAME():
    """Main class.
    """

    def __init__(self):
        self.args = self.parse_arguments()
        self.par_bg_color = ""

    @staticmethod
    def parse_arguments():
        """Parse arguments.

        Returns:
            parser args -- parser argumnents
        """

        parser = argparse.ArgumentParser()
        parser.add_argument('-l', '--character-list',
                            help='character set. See details below',
                            type=str)
        parser.add_argument('-n', '--no-bold',
                            action='store_true',
                            help='do not use bold characters')
        parser.add_argument('-g', '--bg-color',
                            default='default',
                            help='background color (see -c)',
                            type=str)
        parser.add_argument('-v', '--verbose', action='store_true',
                            help='increase output verbosity')

        return parser.parse_args()

    def execute_program(self):
        """Execute the program by arguments.
        """
        # LOGGER.info("Executing")
        if self.args.bg_color is not None:
            self.par_bg_color = self.args.bg_color

        print(self.par_bg_color)

    def sample_function(self, input_str):
        """Sample function

        Arguments:
            input_str {str} -- input string

        Returns:
            str -- result string
        """
        ret = input_str
        return ret


if __name__ == '__main__':
    # LOGGER.debug('Start program')
    PROG = PROJECT_NAME()
    PROG.execute_program()
    # LOGGER.debug('Exit program')
    sys.exit()
