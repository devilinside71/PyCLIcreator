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

LOGGER = logging.getLogger('__PROJECTNAMELCASE__')
# set level for file handling (NOTSET>DEBUG>INFO>WARNING>ERROR>CRITICAL)
LOGGER.setLevel(logging.DEBUG)

# create file handler which logs even debug messages
LOGGER_FH = logging.FileHandler('__PROJECTNAMELCASE__.log')

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


class ProjectName():
    """Main class.
    """

    def __init__(self):
        self.args = self.parse_arguments()
        # __INITARG1__
        # __INITARG2__
        # __INITARG3__
        # __INITARG4__
        # __INITARG5__

    @staticmethod
    def parse_arguments():
        """Parse arguments.

        Returns:
            parser args -- parser argumnents
        """

        parser = argparse.ArgumentParser()
        # __ARG1__
        # __ARG2__
        # __ARG3__
        # __ARG4__
        # __ARG5__
        parser.add_argument('-v', '--verbose', action='store_true',
                            help='increase output verbosity')
        return parser.parse_args()

    def execute_program(self):
        """Execute the program by arguments.
        """
        # __EXECARG1__
        # __EXECARG2__
        # __EXECARG3__
        # __EXECARG4__
        # __EXECARG5__

        # __EXECLOGARG1__
        # __EXECLOGARG2__
        # __EXECLOGARG3__
        # __EXECLOGARG4__
        # __EXECLOGARG5__

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
    PROG = ProjectName()
    PROG.execute_program()
    LOGGER.debug('Exit program')
    sys.exit()
