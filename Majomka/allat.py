# -*- coding: utf-8 -*-
"""

"""

import argparse
import errno
import logging
import os
import sys
# __SQLITEIMPORT__

__author__ = 'Laszlo Tamas'
__copyright__ = '(C) 2027, Laszlo Tamas'
__license__ = 'MIT'
__version__ = '0.0.1'
__maintainer__ = 'Laszlo Tamas'
__email__ = 'noreply@gmail.com'
__status__ = 'Initial'

LOGGER = logging.getLogger('allat')
# set level for file handling (NOTSET>DEBUG>INFO>WARNING>ERROR>CRITICAL)
LOGGER.setLevel(logging.DEBUG)

# create file handler which logs even debug messages
LOGGER_FH = logging.FileHandler('allat.log')

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


class Allat():
    """Main class.
    """

    def __init__(self):
        self.par_input = ''
        self.par_output = ''
        
        
        
        pass

    @staticmethod
    def parse_arguments():
        """Parse arguments.

        Returns:
            parser args -- parser argumnents
        """

        parser = argparse.ArgumentParser()
        parser.add_argument('-i', '--input', help='input file')
        parser.add_argument('-o', '--output', help='output file')
        
        
        
        parser.add_argument('-v', '--verbose', action='store_true',
                            help='increase output verbosity')
        return parser.parse_args()

    def execute_program(self):
        """Execute the program by arguments.
        """
        args = self.parse_arguments()
        if args.input is not None:
            self.par_input = args.input
        if args.output is not None:
            self.par_output = args.output
        
        
        

        LOGGER.debug('input file: %s', self.par_input)
        LOGGER.debug('output file: %s', self.par_output)
        
        
        
        pass

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
    PROG = Allat()
    PROG.execute_program()
    LOGGER.debug('Exit program')
    sys.exit()
