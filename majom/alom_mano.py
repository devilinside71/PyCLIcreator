# -*- coding: utf-8 -*-
"""

"""

import argparse
import errno
import logging
import os
import sys
# __SQLITEIMPORT__

__author__ = 'senki'
__copyright__ = '(C) 2027, senki'
__license__ = 'MIT'
__version__ = '0.0.1'
__maintainer__ = 'senki'
__email__ = 'noreply@gmail.com'
__status__ = 'Initial'

LOGGER = logging.getLogger('alom_mano')
# set level for file handling (NOTSET>DEBUG>INFO>WARNING>ERROR>CRITICAL)
LOGGER.setLevel(logging.DEBUG)

# create file handler which logs even debug messages
LOGGER_FH = logging.FileHandler('alom_mano.log')

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


class Alom_Mano():
    """Main class.
    """

    def __init__(self):
        self.par_exput = ''
        pass

    @staticmethod
    def parse_arguments():
        """Parse arguments.

        Returns:
            parser args -- parser argumnents
        """

        parser = argparse.ArgumentParser()
        parser.add_argument('-e', '--exput', action='store_true', help='external out')
        parser.add_argument('-v', '--verbose', action='store_true',
                            help='increase output verbosity')
        return parser.parse_args()

    def execute_program(self):
        """Execute the program by arguments.
        """
        args = self.parse_arguments()
        if args.exput is not None:
            self.par_exput = args.exput

        LOGGER.debug('external out: %s', self.par_exput)
        pass


if __name__ == '__main__':
    LOGGER.debug('Start program')
    PROG = Alom_Mano()
    PROG.execute_program()
    LOGGER.debug('Exit program')
    sys.exit()
