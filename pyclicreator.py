# -*- coding: utf-8 -*-
"""
This class module is...
"""

import argparse
import errno
import logging
import os
import sys
# __SQLITEIMPORT__

__author__ = 'Laszlo Tamas'
__copyright__ = 'Copyright 2027, Laszlo Tamas'
__license__ = 'GPL'
__version__ = '0.0.1'
__maintainer__ = 'Laszlo Tamas'
__email__ = 'noreply@gmail.com'
__status__ = 'Initial'

LOGGER = logging.getLogger('pyclicreator')
# set level for file handling (NOTSET>DEBUG>INFO>WARNING>ERROR>CRITICAL)
LOGGER.setLevel(logging.DEBUG)

# create file handler which logs even debug messages
LOGGER_FH = logging.FileHandler('pyclicreator.log')

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


class PyCLIcreator():
    """Main class.

    """

    def __init__(self):
        self.par_input = ''
        self.par_output = ''

    @staticmethod
    def parse_arguments():
        """Parse arguments.

        Returns:
            parser args -- parser argumnents
        """

        parser = argparse.ArgumentParser()
        parser.add_argument('-i', '--input',
                            help='input file')
        parser.add_argument('-o', '--output',
                            help='output file')
        parser.add_argument('-v', '--verbose', action='store_true',
                            help='increase output verbosity')
        return parser.parse_args()

    def execute_program(self):
        """Execute the program by arguments.
        """
        args = self.parse_arguments()
        self.par_input = args.input
        self.par_output = args.output
        LOGGER.debug('Input: %s', self.par_input)
        LOGGER.debug('Output: %s', self.par_output)

    def sample_function(self):
        """Sample function
        """
        res = self.par_input
        return res


if __name__ == '__main__':
    LOGGER.debug('Start program')
    PROG = PyCLIcreator()
    PROG.execute_program()
    LOGGER.debug('Exit program')
    sys.exit()
