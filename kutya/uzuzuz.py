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

LOGGER = logging.getLogger('uzuzuz')
# set level for file handling (NOTSET>DEBUG>INFO>WARNING>ERROR>CRITICAL)
LOGGER.setLevel(logging.DEBUG)

# create file handler which logs even debug messages
LOGGER_FH = logging.FileHandler('uzuzuz.log')

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


class Uzuzuz():
    """Main class.
    """

    def __init__(self):
        
        
        
        
        
        pass

    @staticmethod
    def parse_arguments():
        """Parse arguments.

        Returns:
            parser args -- parser argumnents
        """

        parser = argparse.ArgumentParser()
        
        
        
        
        
        parser.add_argument('-v', '--verbose', action='store_true',
                            help='increase output verbosity')
        return parser.parse_args()

    def execute_program(self):
        """Execute the program by arguments.
        """
        args = self.parse_arguments()
        
        
        
        
        

        
        
        
        
        
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
    PROG = Uzuzuz()
    PROG.execute_program()
    LOGGER.debug('Exit program')
    sys.exit()
