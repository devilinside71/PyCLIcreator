# -*- coding: utf-8 -*-
"""
Create Python3 CLI project
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
        self.par_name = ''
        self.par_description = ''
        self.par_author = 'Laszlo Tamas'
        self.par_copyright = '(C) 2027'
        self.par_folder = ''
        self.par_version = '0.0.1'
        self.par_sqlite = False
        self.par_template = 'sample_01.py'

        self.gui_needed = False
        self.main_filename = ''
        self.test_filename = ''
        self.readme_filename = ''

    @staticmethod
    def parse_arguments():
        """Parse arguments.

        Returns:
            parser args -- parser argumnents
        """

        parser = argparse.ArgumentParser()
        parser.add_argument('-n', '--name',
                            help='project name')
        parser.add_argument('-d', '--description',
                            help='project description')
        parser.add_argument('-a', '--author',
                            help='project auhtor')
        parser.add_argument('-c', '--copyright',
                            help='copyright note')
        parser.add_argument('-f', '--folder',
                            help='project folder')
        parser.add_argument('-v', '--version',
                            help='project version number')
        parser.add_argument('-s', '--sqlite', action='store_true',
                            help='sqlite functionality')
        parser.add_argument('-t', '--template',
                            help='template filename')
        parser.add_argument('-a1s', '--arg1short',
                            help='arg1 short name')
        parser.add_argument('-a1l', '--arg1long',
                            help='arg1 long name')
        parser.add_argument('-a1h', '--arg1help',
                            help='arg1 help text')
        parser.add_argument('-a1b', '--arg1bool',
                            action='store_true', help='arg1 is boolean')
        return parser.parse_args()

    def execute_program(self):
        """Execute the program by arguments.
        """
        args = self.parse_arguments()
        if args.name is not None:
            self.par_name = args.name
        if args.description is not None:
            self.par_description = args.description
        if args.author is not None:
            self.par_author = args.author
        if args.copyright is not None:
            self.par_copyright = args.copyright
        if args.folder is not None:
            self.par_folder = args.folder
        if args.version is not None:
            self.par_version = args.version
        if args.sqlite is not None:
            self.par_sqlite = args.sqlite
        if args.template is not None:
            self.par_template = args.template
        LOGGER.debug('Name: %s', self.par_name)
        LOGGER.debug('Description: %s', self.par_description)
        LOGGER.debug('Author: %s', self.par_author)
        LOGGER.debug('Copyright: %s', self.par_copyright)
        LOGGER.debug('Folder: %s', self.par_folder)
        LOGGER.debug('Version: %s', self.par_version)
        LOGGER.debug('SQLite: %s', self.par_sqlite)
        LOGGER.debug('Template: %s', self.par_template)
        self.check_if_gui_needed()

    def check_if_gui_needed(self):
        """Check if GUI needed becacuse of missing parameters.
        """
        self.gui_needed = False
        if self.par_name == '' or self.par_folder == '':
            self.gui_needed = True
        LOGGER.debug('GUI needed: %s', self.gui_needed)


if __name__ == '__main__':
    LOGGER.debug('Start program')
    PROG = PyCLIcreator()
    PROG.execute_program()
    LOGGER.debug('Exit program')
    sys.exit()
