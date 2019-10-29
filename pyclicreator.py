# -*- coding: utf-8 -*-
"""
Create Python3 CLI project
"""

import argparse
import errno
import logging
import os
import sys
from textformatter import TextFormatter, FormatType
from pycligui import PyCLIGUI

__author__ = 'Laszlo Tamas'
__copyright__ = 'Copyright 2027, Laszlo Tamas'
__license__ = 'MIT'
__version__ = '0.1.1'
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
        self.text_formatter = TextFormatter()
        self.args = self.parse_arguments()
        self.gui = PyCLIGUI()

        self.par_name = ''
        self.par_description = ''
        self.par_author = 'Laszlo Tamas'
        self.par_copyright = '(C) 2027'
        self.par_folder = ''
        self.par_version = '0.0.1'
        self.par_sqlite = True
        self.par_template = 'sample_01.py'
        self.par_testtemplate = 'sample_01_test.py'
        self.par_notestemplate = 'sample_01_notes.txt'
        self.par_licence = 'MIT'
        self.par_email = 'noreply@gmail.com'
        self.par_status = 'Initial'
        self.par_forcegui = False
        self.par_predefined = ''

        self.par_arg1s = ''
        self.par_arg1l = ''
        self.par_arg1help = ''
        self.par_arg1bool = False

        self.par_arg2s = ''
        self.par_arg2l = ''
        self.par_arg2help = ''
        self.par_arg2bool = False

        self.par_arg3s = ''
        self.par_arg3l = ''
        self.par_arg3help = ''
        self.par_arg3bool = False

        self.par_arg4s = ''
        self.par_arg4l = ''
        self.par_arg4help = ''
        self.par_arg4bool = False

        self.par_arg5s = ''
        self.par_arg5l = ''
        self.par_arg5help = ''
        self.par_arg5bool = False

        self.gui_needed = False
        self.main_filename = ''
        self.test_filename = ''
        self.notes_filename = ''
        self.class_name = ''
        self.folder_created_by_dialog = True

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
        parser.add_argument('-g', '--gui',
                            help='force gui mode')
        parser.add_argument('-p', '--predefined',
                            help='predefined settings >> IO:input-output file')
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

        parser.add_argument('-a2s', '--arg2short',
                            help='arg2 short name')
        parser.add_argument('-a2l', '--arg2long',
                            help='arg2 long name')
        parser.add_argument('-a2h', '--arg2help',
                            help='arg2 help text')
        parser.add_argument('-a2b', '--arg2bool',
                            action='store_true', help='arg2 is boolean')

        parser.add_argument('-a3s', '--arg3short',
                            help='arg3 short name')
        parser.add_argument('-a3l', '--arg3long',
                            help='arg3 long name')
        parser.add_argument('-a3h', '--arg3help',
                            help='arg3 help text')
        parser.add_argument('-a3b', '--arg3bool',
                            action='store_true', help='arg3 is boolean')

        parser.add_argument('-a4s', '--arg4short',
                            help='arg4 short name')
        parser.add_argument('-a4l', '--arg4long',
                            help='arg4 long name')
        parser.add_argument('-a4h', '--arg4help',
                            help='arg4 help text')
        parser.add_argument('-a4b', '--arg4bool',
                            action='store_true', help='arg4 is boolean')

        parser.add_argument('-a5s', '--arg5short',
                            help='arg5 short name')
        parser.add_argument('-a5l', '--arg5long',
                            help='arg5 long name')
        parser.add_argument('-a5h', '--arg5help',
                            help='arg5 help text')
        parser.add_argument('-a5b', '--arg5bool',
                            action='store_true', help='arg5 is boolean')

        return parser.parse_args()

    def execute_program(self):
        """Execute the program by arguments.
        """
        if self.args.name is not None:
            self.par_name = self.args.name
        if self.args.description is not None:
            self.par_description = self.args.description
        if self.args.author is not None:
            self.par_author = self.args.author
        if self.args.copyright is not None:
            self.par_copyright = self.args.copyright
        if self.args.folder is not None:
            self.par_folder = self.args.folder
        if self.args.version is not None:
            self.par_version = self.args.version
        if self.args.sqlite is not None:
            self.par_sqlite = self.args.sqlite
        if self.args.template is not None:
            self.par_template = self.args.template
        if self.args.testtemplate is not None:
            self.par_testtemplate = self.args.testtemplate
        if self.args.licence is not None:
            self.par_licence = self.args.licence
        if self.args.email is not None:
            self.par_email = self.args.email
        if self.args.status is not None:
            self.par_status = self.args.status
        if self.args.gui is not None:
            self.par_forcegui = self.args.gui
        if self.args.predefined is not None:
            self.par_predefined = self.args.predefined

        if self.args.arg1short is not None:
            self.par_arg1s = self.args.arg1short
        if self.args.arg1long is not None:
            self.par_arg1l = self.args.arg1long
        if self.args.arg1help is not None:
            self.par_arg1help = self.args.arg1help
        if self.args.arg1bool is not None:
            self.par_arg1bool = self.args.arg1bool

        if self.args.arg2short is not None:
            self.par_arg2s = self.args.arg2short
        if self.args.arg2long is not None:
            self.par_arg2l = self.args.arg2long
        if self.args.arg2help is not None:
            self.par_arg2help = self.args.arg2help
        if self.args.arg2bool is not None:
            self.par_arg2bool = self.args.arg2bool

        if self.args.arg3short is not None:
            self.par_arg3s = self.args.arg3short
        if self.args.arg3long is not None:
            self.par_arg3l = self.args.arg3long
        if self.args.arg3help is not None:
            self.par_arg3help = self.args.arg3help
        if self.args.arg3bool is not None:
            self.par_arg3bool = self.args.arg3bool

        if self.args.arg4short is not None:
            self.par_arg4s = self.args.arg4short
        if self.args.arg4long is not None:
            self.par_arg4l = self.args.arg4long
        if self.args.arg4help is not None:
            self.par_arg4help = self.args.arg4help
        if self.args.arg4bool is not None:
            self.par_arg4bool = self.args.arg4bool

        if self.args.arg5short is not None:
            self.par_arg5s = self.args.arg5short
        if self.args.arg5long is not None:
            self.par_arg5l = self.args.arg5long
        if self.args.arg5help is not None:
            self.par_arg5help = self.args.arg5help
        if self.args.arg5bool is not None:
            self.par_arg5bool = self.args.arg5bool

        self.create_main_filename()
        self.create_test_filename()
        self.create_notes_filename()
        self.create_class_name()

        self.log_parameters()

        self.is_gui_needed()
        if self.gui_needed:
            self.setup_gui_variables()
            self.gui.create_gui()
            self.par_name = self.gui.par_name
            self.par_description = self.gui.par_description
            self.par_author = self.gui.par_author
            self.par_copyright = self.gui.par_copyright
            self.par_folder = self.gui.par_folder
            self.par_version = self.gui.par_version
            self.par_template = self.gui.par_template
            self.par_testtemplate = self.gui.par_testtemplate
            self.par_notestemplate = self.gui.par_notestemplate
            self.par_licence = self.gui.par_licence
            self.par_email = self.gui.par_email
            self.par_status = self.gui.par_status

            self.par_arg1s = self.gui.par_arg1s
            self.par_arg1l = self.gui.par_arg1l
            self.par_arg1help = self.gui.par_arg1help
            self.par_arg1bool = self.gui.par_arg1bool
            self.par_arg2s = self.gui.par_arg2s
            self.par_arg2l = self.gui.par_arg2l
            self.par_arg2help = self.gui.par_arg2help
            self.par_arg2bool = self.gui.par_arg2bool
            self.par_arg3s = self.gui.par_arg3s
            self.par_arg3l = self.gui.par_arg3l
            self.par_arg3help = self.gui.par_arg3help
            self.par_arg3bool = self.gui.par_arg3bool
            self.par_arg4s = self.gui.par_arg4s
            self.par_arg4l = self.gui.par_arg4l
            self.par_arg4help = self.gui.par_arg4help
            self.par_arg4bool = self.gui.par_arg4bool
            self.par_arg5s = self.gui.par_arg5s
            self.par_arg5l = self.gui.par_arg5l
            self.par_arg5help = self.gui.par_arg5help
            self.par_arg5bool = self.gui.par_arg5bool

            self.create_main_filename()
            self.create_test_filename()
            self.create_notes_filename()
            self.create_class_name()

            self.log_parameters()

        self.create_project()

    def setup_gui_general_variables(self):
        """Setup GUI general variables.
        """
        self.gui.par_name = self.par_name
        self.gui.par_description = self.par_description
        self.gui.par_author = self.par_author
        self.gui.par_copyright = self.par_copyright
        self.gui.par_folder = self.par_folder
        self.gui.par_version = self.par_version
        self.gui.par_sqlite = self.par_sqlite
        self.gui.par_template = self.par_template
        self.gui.par_testtemplate = self.par_testtemplate
        self.gui.par_notestemplate = self.par_notestemplate
        self.gui.par_licence = self.par_licence
        self.gui.par_email = self.par_email
        self.gui.par_status = self.par_status
        self.gui.par_forcegui = self.par_forcegui
        self.gui.par_predefined = self.par_predefined



    def setup_gui_variables(self):
        """Setup GUI variables before showing.
        """
        self.setup_gui_general_variables()
        if self.par_predefined != '':
            if self.par_predefined == 'IO':
                self.gui.par_arg1s = 'i'
                self.gui.par_arg1l = 'input'
                self.gui.par_arg1help = 'input file'
                self.gui.par_arg2s = 'o'
                self.gui.par_arg2l = 'output'
                self.gui.par_arg2help = 'output file'
        else:
            self.gui.par_arg1s = self.par_arg1s
            self.gui.par_arg1l = self.par_arg1l
            self.gui.par_arg1help = self.par_arg1help
            self.gui.par_arg1bool = self.par_arg1bool

            self.gui.par_arg2s = self.par_arg2s
            self.gui.par_arg2l = self.par_arg2l
            self.gui.par_arg2help = self.par_arg2help
            self.gui.par_arg2bool = self.par_arg2bool

            self.gui.par_arg3s = self.par_arg3s
            self.gui.par_arg3l = self.par_arg3l
            self.gui.par_arg3help = self.par_arg3help
            self.gui.par_arg3bool = self.par_arg3bool

            self.gui.par_arg4s = self.par_arg4s
            self.gui.par_arg4l = self.par_arg4l
            self.gui.par_arg4help = self.par_arg4help
            self.gui.par_arg4bool = self.par_arg4bool

            self.gui.par_arg5s = self.par_arg5s
            self.gui.par_arg5l = self.par_arg5l
            self.gui.par_arg5help = self.par_arg5help
            self.gui.par_arg5bool = self.par_arg5bool

    def log_parameters(self):
        """Write log for all parameters.
        """
        LOGGER.debug('Name: %s', self.par_name)
        LOGGER.debug('Description: %s', self.par_description)
        LOGGER.debug('Author: %s', self.par_author)
        LOGGER.debug('Copyright: %s', self.par_copyright)
        LOGGER.debug('Folder: %s', self.par_folder)
        LOGGER.debug('Version: %s', self.par_version)
        LOGGER.debug('SQLite: %s', self.par_sqlite)
        LOGGER.debug('Template: %s', self.par_template)
        LOGGER.debug('Test template: %s', self.par_testtemplate)
        LOGGER.debug('Licence: %s', self.par_licence)
        LOGGER.debug('Email: %s', self.par_email)
        LOGGER.debug('Status: %s', self.par_status)
        LOGGER.debug('Force GUI mode: %s', self.par_forcegui)
        LOGGER.debug('Main filename: %s', self.main_filename)
        LOGGER.debug('Test filename: %s', self.test_filename)
        LOGGER.debug('Notes filename: %s', self.notes_filename)
        LOGGER.debug('Class name: %s', self.class_name)
        LOGGER.debug('Predefined: %s', self.par_predefined)
        LOGGER.debug('ARG1: %s', self.par_arg1s+'|'+self.par_arg1l +
                     '|'+self.par_arg1help+'|'+str(self.par_arg1bool))
        LOGGER.debug('ARG2: %s', self.par_arg2s+'|'+self.par_arg2l +
                     '|'+self.par_arg2help+'|'+str(self.par_arg2bool))
        LOGGER.debug('ARG3: %s', self.par_arg3s+'|'+self.par_arg3l +
                     '|'+self.par_arg3help+'|'+str(self.par_arg3bool))
        LOGGER.debug('ARG4: %s', self.par_arg4s+'|'+self.par_arg4l +
                     '|'+self.par_arg4help+'|'+str(self.par_arg4bool))
        LOGGER.debug('ARG5: %s', self.par_arg5s+'|'+self.par_arg5l +
                     '|'+self.par_arg5help+'|'+str(self.par_arg5bool))

    def create_project(self):
        """Create project.
        """

        if self.create_folder(self.par_folder) or self.folder_created_by_dialog:
            # Create main file
            with open(self.par_template, 'r') as myfile:
                data = myfile.read()
                data = self.replace_general_data(data)
                if self.par_predefined != '':
                    if self.par_predefined == 'IO':
                        data = data.replace(
                            '# __ARG1__', self.get_arg_line('i', 'input', 'input file', False))
                        data = data.replace(
                            '# __INITARG1__', self.get_init_arg_line('input'))
                        data = data.replace(
                            '# __EXECARG1__', self.get_exec_arg_line('input'))
                        data = data.replace(
                            '# __EXECLOGARG1__',
                            self.get_execlog_arg_line('input file', 'input'))
                        data = data.replace(
                            '# __ARG2__', self.get_arg_line('o', 'output', 'output file', False))
                        data = data.replace(
                            '# __INITARG2__', self.get_init_arg_line('output'))
                        data = data.replace(
                            '# __EXECARG2__', self.get_exec_arg_line('output'))
                        data = data.replace(
                            '# __EXECLOGARG2__',
                            self.get_execlog_arg_line('output file', 'output'))
                        data = data.replace('# __ARG3__', '')
                        data = data.replace('# __INITARG3__', '')
                        data = data.replace('# __EXECARG3__', '')
                        data = data.replace('# __EXECLOGARG3__', '')
                        data = data.replace('# __ARG4__', '')
                        data = data.replace('# __INITARG4__', '')
                        data = data.replace('# __EXECARG4__', '')
                        data = data.replace('# __EXECLOGARG4__', '')
                        data = data.replace('# __ARG5__', '')
                        data = data.replace('# __INITARG5__', '')
                        data = data.replace('# __EXECARG5__', '')
                        data = data.replace('# __EXECLOGARG5__', '')

                else:
                    data = self.replace_arg_data(
                        data, '1', self.par_arg1s, self.par_arg1l, self.par_arg1help,
                        self.par_arg1bool)
                    data = self.replace_arg_data(
                        data, '2', self.par_arg2s, self.par_arg2l, self.par_arg2help,
                        self.par_arg2bool)
                    data = self.replace_arg_data(
                        data, '3', self.par_arg3s, self.par_arg3l, self.par_arg3help,
                        self.par_arg3bool)
                    data = self.replace_arg_data(
                        data, '4', self.par_arg4s, self.par_arg4l, self.par_arg4help,
                        self.par_arg4bool)
                    data = self.replace_arg_data(
                        data, '5', self.par_arg5s, self.par_arg5l, self.par_arg5help,
                        self.par_arg5bool)

                # print(data)
                text_file = open(self.main_filename, 'w', encoding='utf-8')
                text_file.write(data)
                text_file.close()
            self.create_unittest_file()
            self.create_notes_file()

    def replace_arg_data(self, data, argnumber, argushort, argulong, arguhelp, argubool):
        """Replace arg data.

        Arguments:
            data {str} -- data
            argnumber {str} -- number of argument
            argushort {str} -- short name
            argulong {str} -- long name
            arguhelp {str} -- help text
            argubool {bool} -- boolean

        Returns:
            str -- modified data
        """
        if self.is_arg_valid(argushort, argulong, arguhelp):
            data = data.replace(
                '# __ARG'+argnumber+'__',
                self.get_arg_line(argushort,
                                  argulong, arguhelp,
                                  argubool))
            data = data.replace(
                '# __INITARG'+argnumber+'__', self.get_init_arg_line(
                    argulong))
            data = data.replace(
                '# __EXECARG'+argnumber+'__', self.get_exec_arg_line(argulong))
            data = data.replace(
                '# __EXECLOGARG'+argnumber+'__',
                self.get_execlog_arg_line(arguhelp, argulong))
        else:
            data = data.replace('# __ARG'+argnumber+'__', '')
            data = data.replace('# __INITARG'+argnumber+'__', '')
            data = data.replace('# __EXECARG'+argnumber+'__', '')
            data = data.replace('# __EXECLOGARG'+argnumber+'__', '')
        return data

    def replace_general_data(self, data):
        """Replace general project data.

        Arguments:
            data {str} -- data

        Returns:
            str -- modified data
        """
        data = data.replace('__AUTHOR__', self.par_author)
        data = data.replace('ProjectName()',
                            self.class_name+'()')
        data = data.replace('__PROJECTNAMELCASE__',
                            self.class_name.lower())
        data = data.replace('__DESCRIPTION__', self.par_description)
        data = data.replace('__COPYRIGHT__', self.par_copyright)
        data = data.replace('__LICENCE__', self.par_licence)
        data = data.replace('__VERSION__', self.par_version)
        data = data.replace('__EMAIL__', self.par_email)
        data = data.replace('__STATUS__', self.par_status)
        return data

    def create_unittest_file(self):
        """Create unittest.
        """
        with open(self.par_testtemplate, 'r') as myfile:
            data = myfile.read()
            data = data.replace('__PROJECTNAME__', self.class_name)
            data = data.replace('__PROJECTNAMELCASE__',
                                self.class_name.lower())
            data = data.replace('__DESCRIPTION__', self.par_description)
            # print(data)
            text_file = open(self.test_filename, 'w', encoding='utf-8')
            text_file.write(data)
            text_file.close()

    def create_notes_file(self):
        """Create notes txt file for running commands.
        """
        with open(self.par_notestemplate, 'r') as myfile:
            data = myfile.read()
            data = data.replace('__PROJECTNAME__', self.class_name)
            data = data.replace('__PROJECTNAMELCASE__',
                                self.class_name.lower())
            data = data.replace('__DESCRIPTION__', self.par_description)
            # print(data)
            text_file = open(self.notes_filename, 'w', encoding='utf-8')
            text_file.write(data)
            text_file.close()

    def is_gui_needed(self):
        """Check if GUI needed becacuse of missing parameters.
        """
        self.gui_needed = False
        if self.par_name == '' or self.par_folder == '' or self.par_forcegui:
            self.gui_needed = True
        LOGGER.debug('GUI needed: %s', self.gui_needed)

    @staticmethod
    def is_arg_valid(argshort, arglong, arghelp):
        """Check if arg is valid

        Arguments:
            argshort {str} -- short name
            arglong {str} -- long name
            arghelp {str} -- help text

        Returns:
            bool -- arg is valid or not
        """
        ret = False
        if argshort != '' and arglong != '' and arghelp != '':
            if argshort is not None and arglong is not None and arghelp is not None:
                ret = True
        return ret

    def create_main_filename(self):
        """Create main project filename.
        """
        self.main_filename = self.text_formatter.get_normalized_name(
            self.par_name, FormatType.FILENAME)+'.py'
        self.main_filename = self.par_folder+'/'+self.main_filename

    def create_test_filename(self):
        """Create unittest filename.
        """
        self.test_filename = self.text_formatter.get_normalized_name(
            self.par_name, FormatType.FILENAME)+'_test.py'
        self.test_filename = self.par_folder+'/'+self.test_filename

    def create_notes_filename(self):
        """Create notes.txt with command line examples.
        """
        self.notes_filename = self.text_formatter.get_normalized_name(
            self.par_name, FormatType.FILENAME)+'_notes.txt'
        self.notes_filename = self.par_folder+'/'+self.notes_filename

    def create_class_name(self):
        """Create class name.
        """
        self.class_name = self.text_formatter.get_normalized_name(
            self.par_name, FormatType.CLASSNAME)

    @staticmethod
    def get_arg_line(argshort, arglong, arghelp, argbool):
        """Create argumentum line.

        Arguments:
            argshort {str} -- short name
            arglong {str} -- long name
            arghelp {str} -- help text
            argbool {bool} -- boolean type

        Returns:
            str -- args line
        """
        ret = ''
        if argshort != '' and arglong != '' and arghelp != '':
            if argshort is not None and arglong is not None and arghelp is not None:
                ret = 'parser.add_argument(\'-' + \
                    argshort+'\', \'--'+arglong+'\', '
                if argbool:
                    ret += 'action=\'store_true\', '
                ret += 'help=\''+arghelp+'\')'
        return ret

    @staticmethod
    def get_execlog_arg_line(arghelp, arglong):
        """Create LOGGER line

        Arguments:
            arghelp {str} -- help text
            arglong {str} -- long name

        Returns:
            str -- LOGGER line
        """
        ret = ''
        if arglong != '' and arglong is not None and arghelp != '' and arghelp is not None:
            ret = 'LOGGER.debug(\''+arghelp+': %s\', self.par_'+arglong+')'
        return ret

    @staticmethod
    def get_exec_arg_line(arglong):
        """Create execute arg line

        Arguments:
            arglong {str} -- long name

        Returns:
            str -- execute args line
        """
        ret = ''
        if arglong != '' and arglong is not None:
            ret = 'if self.args.'+arglong+' is not None:\n            self.par_' + \
                arglong+' = self.args.'+arglong
        return ret

    @staticmethod
    def get_init_arg_line(arglong):
        """Create init argumentum line

        Arguments:
            arglong {str} -- long name

        Returns:
            str -- init args line
        """
        ret = ''
        if arglong != '' and arglong is not None:
            ret = 'self.par_'+arglong+' = \'\''
        return ret

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


if __name__ == '__main__':
    LOGGER.debug('Start program')
    PROG = PyCLIcreator()
    PROG.execute_program()
    LOGGER.debug('Exit program')
    sys.exit()
