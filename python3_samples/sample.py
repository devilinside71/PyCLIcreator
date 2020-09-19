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

LOGGER = logging.getLogger('PROJECT_NAME')
# set level for file handling (NOTSET>DEBUG>INFO>WARNING>ERROR>CRITICAL)
LOGGER.setLevel(logging.DEBUG)

# create file handler which logs even debug messages
LOGGER_FH = logging.FileHandler('PROJECT_NAME.log')

# create console handler with a higher log level
LOGGER_CH = logging.StreamHandler()
LOGGER_CH.setLevel(logging.INFO)

# create FORMATTER and add it to the handlers
FORMATTER = \
    logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'
                      )
LOGGER_FH.setFormatter(FORMATTER)
LOGGER_CH.setFormatter(FORMATTER)

# add the handlers to the LOGGER
LOGGER.addHandler(LOGGER_FH)
LOGGER.addHandler(LOGGER_CH)

help_msg = '''
USAGE
  PROJECT_NAME [-a] [-b] [-c COLOR] [-f] [-g COLOR] [-h] [-l CHARACTER_LIST] [-n]
            [-o] [-s SPEED] [-u CUSTOM_CHARACTERS]
OPTIONAL ARGUMENTS
  -a                   Asynchronous scroll. Lines will move at varied speeds.

  -b                   Use only bold characters

  -c COLOR             One of: green (default), red, blue, white, yellow, cyan,
                       magenta, black

  -f                   Enable "flashers," characters that continuously change.

  -g COLOR             Background color (See -c). Defaults to keeping
                       terminal's current background.

  -h                   Show this help message and exit

LONG ARGUMENTS
  -a --asynchronous
  -b --all-bold
  -c --color=COLOR
  -f --flashers
  -g --bg-color=COLOR
  -h --help
  -l --character-list=CHARACTER_LIST
  -s --speed=SPEED
  -n --no-bold
  -o --status-off
  -t --time
  -u --custom_characters=CUSTOM_CHARACTERS
  -w --single_wave

EXAMPLES
  Mimic default output of cmatrix (no unicode characters, works in TTY):
    $ PROJECT_NAME -n -s 96 -l o

  Use the letters from the name of your favorite operating system in bold blue:
    $ PROJECT_NAME -B -u Linux -c blue
'''

# Set up parser and apply arguments settings


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

        parser = argparse.ArgumentParser(add_help=False)
        # parser = argparse.ArgumentParser()
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
        parser.add_argument('-h', '--help',
                            help='display extended usage information and exit',
                            action='store_true')
        parser.add_argument('-v', '--verbose', action='store_true',
                            help='increase output verbosity')
        if parser.parse_args().help:
            print(help_msg)
            exit()
        return parser.parse_args()

    def execute_program(self):
        """Execute the program by arguments.
        """
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
    LOGGER.debug('Start program')
    PROG = PROJECT_NAME()
    PROG.execute_program()
    LOGGER.debug('Exit program')
    sys.exit()
