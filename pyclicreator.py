# -*- coding: utf-8 -*-
"""
Create Python3 CLI project
"""

import argparse
import errno
import logging
import os
import sys
from tkinter import Label, Entry, Button, W, END, Tk, filedialog

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
        self.par_testemplate = 'sample_01_test.py'
        self.par_licence = 'MIT'
        self.par_email = 'noreply@gmail.com'
        self.par_status = 'Initial'

        self.gui_needed = False
        self.main_filename = ''
        self.test_filename = ''
        self.notes_filename = ''
        self.class_name = ''
        self.folder_created_by_dialog = True

        self.master = Tk()
        self.entry_folder = Entry(self.master)
        self.entry_name = Entry(self.master)
        self.entry_description = Entry(self.master)
        self.entry_author = Entry(self.master)
        self.entry_copyright = Entry(self.master)
        self.entry_version = Entry(self.master)
        self.entry_template = Entry(self.master)
        self.entry_testtemplate = Entry(self.master)
        self.entry_licence = Entry(self.master)
        self.entry_email = Entry(self.master)
        self.entry_status = Entry(self.master)
        # TODO SQLite checkbox

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
        parser.add_argument('-tt', '--testtemplate',
                            help='test template filename')
        parser.add_argument('-l', '--licence',
                            help='licence type')
        parser.add_argument('-e', '--email',
                            help='email of the author')
        parser.add_argument('-st', '--status',
                            help='status of the project')
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
        if args.testtemplate is not None:
            self.par_testemplate = args.testtemplate
        if args.licence is not None:
            self.par_licence = args.licence
        if args.email is not None:
            self.par_email = args.email
        if args.status is not None:
            self.par_status = args.status
        LOGGER.debug('Name: %s', self.par_name)
        LOGGER.debug('Description: %s', self.par_description)
        LOGGER.debug('Author: %s', self.par_author)
        LOGGER.debug('Copyright: %s', self.par_copyright)
        LOGGER.debug('Folder: %s', self.par_folder)
        LOGGER.debug('Version: %s', self.par_version)
        LOGGER.debug('SQLite: %s', self.par_sqlite)
        LOGGER.debug('Template: %s', self.par_template)
        LOGGER.debug('Test template: %s', self.par_testemplate)
        LOGGER.debug('Licence: %s', self.par_licence)
        LOGGER.debug('Email: %s', self.par_email)
        LOGGER.debug('Status: %s', self.par_status)
        self.check_if_gui_needed()

        self.create_main_filename()
        self.create_test_filename()
        self.create_notes_filename()
        self.create_class_name()
        LOGGER.debug('Main filename: %s', self.main_filename)
        LOGGER.debug('Test filename: %s', self.test_filename)
        LOGGER.debug('Notes filename: %s', self.notes_filename)
        LOGGER.debug('Class name: %s', self.class_name)

        if self.create_folder(self.par_folder) or self.folder_created_by_dialog:
            # Create main file
            with open(self.par_template, 'r') as myfile:
                data = myfile.read()
                data = data.replace('__AUTHOR__', self.par_author)
                data = data.replace('__PROJECTNAME__',
                                    self.class_name)
                data = data.replace('__PROJECTNAMELCASE__',
                                    self.class_name.lower())
                data = data.replace('__DESCRIPTION__', self.par_description)
                data = data.replace('__COPYRIGHT__', self.par_copyright)
                data = data.replace('__LICENCE__', self.par_licence)
                data = data.replace('__VERSION__', self.par_version)
                data = data.replace('__EMAIL__', self.par_email)
                data = data.replace('__STATUS__', self.par_status)

                # print(data)
                text_file = open(self.main_filename, 'w',
                                 encoding='utf-8')
                text_file.write(data)
                text_file.close()
            # Create unittest file
            with open(self.par_testemplate, 'r') as myfile:
                data = myfile.read()
                data = data.replace('__PROJECTNAME__',
                                    self.class_name)
                data = data.replace('__PROJECTNAMELCASE__',
                                    self.class_name.lower())
                data = data.replace('__DESCRIPTION__', self.par_description)
                # print(data)
                text_file = open(self.test_filename, 'w',
                                 encoding='utf-8')
                text_file.write(data)
                text_file.close()

    def check_if_gui_needed(self):
        """Check if GUI needed becacuse of missing parameters.
        """
        self.gui_needed = False
        if self.par_name == '' or self.par_folder == '':
            self.gui_needed = True
        LOGGER.debug('GUI needed: %s', self.gui_needed)

    def create_main_filename(self):
        """Create main project filename.
        """
        self.main_filename = self.get_normalized_name(
            self.par_name, 'filename')+'.py'
        self.main_filename = self.par_folder+'/'+self.main_filename

    def create_test_filename(self):
        """Create unittest filename.
        """
        self.test_filename = self.get_normalized_name(
            self.par_name, 'filename')+'_test.py'
        self.test_filename = self.par_folder+'/'+self.test_filename

    def create_notes_filename(self):
        """Create notes.txt for command line examples.
        """
        self.notes_filename = self.get_normalized_name(
            self.par_name, 'filename')+'_notes.txt'

    def create_class_name(self):
        """Create class name.
        """
        self.class_name = self.get_normalized_name(self.par_name, 'classname')

    @staticmethod
    def get_normalized_name(name_str, mode):
        """Replace non US characters

        Arguments:
            name_str {str} -- string to normalize
            mode {str} -- conversion mode
                          normal -- replace non US chars
                          filename -- no space and lowercase
                          classname -- PascalCase
        Returns:
            str -- normalized string
        """

        res = name_str
        res = res.replace('á', 'a')
        res = res.replace('Á', 'A')
        res = res.replace('é', 'e')
        res = res.replace('É', 'E')
        res = res.replace('ö', 'o')
        res = res.replace('Ö', 'O')
        res = res.replace('ő', 'o')
        res = res.replace('Ő', 'O')
        res = res.replace('ó', 'o')
        res = res.replace('Ó', 'O')
        res = res.replace('ü', 'u')
        res = res.replace('Ü', 'U')
        res = res.replace('ű', 'u')
        res = res.replace('Ű', 'U')
        res = res.replace('ú', 'u')
        res = res.replace('Ú', 'U')
        res = res.replace('í', 'i')
        res = res.replace('Í', 'i')
        if mode != 'normal':
            res = res.replace(' ', '_')
            res = res.replace('.', '_')
            res = res.replace(':', '_')
        if mode == 'filename':
            res = res.lower()
        if mode == 'classname':
            full_res = ''
            parts = res.split('_')
            for part in parts:
                full_res += part.capitalize()+'_'
            res = full_res[:-1]
        return res

    @staticmethod
    def create_folder(folder_name):
        """Create folder for new project.

        Arguments:
            folder_name {str} -- target folder name

        Returns:
            bool -- folder created succesfuly
        """
        ret = False
        LOGGER.debug('Target folder: %s', folder_name)
        # Check if folder exists
        folder_exists = os.path.isdir(folder_name)
        if folder_exists:
            LOGGER.debug('Folder "%s" already exists', folder_name)
        else:
            # create folder
            try:
                os.makedirs(folder_name)
                LOGGER.debug('Folder "%s" created succesfuly', folder_name)
                ret = True
            except OSError as os_err:
                ret = False
                if os_err.errno != errno.EEXIST:
                    LOGGER.debug('Cannot create folder %s', folder_name)
                    LOGGER.debug('Exit program')
                    raise
        return ret

    def set_folder(self):
        """Set the project folder by filedialog.
        """

        self.par_folder = filedialog.askdirectory()
        self.entry_folder.delete(0, END)
        self.entry_folder.insert(0, self.par_folder)
        LOGGER.debug('Folder: %s', self.par_folder)
        self.folder_created_by_dialog = True


if __name__ == '__main__':
    LOGGER.debug('Start program')
    PROG = PyCLIcreator()
    PROG.execute_program()
    LOGGER.debug('Exit program')
    sys.exit()
