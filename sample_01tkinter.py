# -*- coding: utf-8 -*-
"""
__DESCRIPTION__
"""

import argparse
import errno
import logging
import os
import sys
from tkinter import Label, Entry, Button, Checkbutton, W, E, END, Tk, filedialog, BooleanVar

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
LOGGER_FH = logging.FileHandler('__PROJECTNAMELCASE__.log', 'w', 'utf-8')

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
        self.folder_created_by_dialog = False
        self.file_created_by_dialog = False

        self.master = Tk()
        # __INITARG1__
        # __INITARG2__
        # __INITARG3__
        # __INITARG4__
        # __INITARG5__
        self.par_folder = ''
        self.par_file = ''
        self.par_b = BooleanVar()
        self.par_bool = False

        self.entry_folder = Entry(self.master)
        self.entry_file = Entry(self.master)
        self.chk_bool = Checkbutton(
            self.master, text="Bool", variable=self.par_b)
        self.btn_ok = Button(self.master, text='OK',
                             command=self.execute_ok)
        self.btn_cancel = Button(
            self.master, text='Cancel', command=self.master.quit)

    def execute_ok(self):
        """Execute OK button.
        """

    def create_gui(self):
        """Create GUI.
        """
        Label(self.master, text='Folder Name').grid(row=0, sticky=E+W)
        self.entry_folder.delete(0, END)
        self.entry_folder.insert(0, self.par_folder)
        self.entry_folder.grid(row=0, column=1, columnspan=3, sticky=W)
        self.entry_folder.config(width=70)
        Button(self.master, text='Browse', command=self.set_folder).grid(
            row=0, column=4, sticky=W, pady=4)

        Label(self.master, text='File name').grid(row=1, column=0, sticky=E)
        self.entry_file.delete(0, END)
        self.entry_file.insert(0, self.par_file)
        self.entry_file.grid(row=1, column=1, columnspan=3, sticky=W)
        self.entry_file.config(width=70)
        Button(self.master, text='Browse', command=self.set_file).grid(
            row=1, column=4, sticky=W, pady=4)

        self.chk_bool.grid(row=12, column=4)

        self.btn_cancel.grid(row=18, column=0, sticky=W)
        self.btn_ok.grid(row=18, column=2, sticky=W, columnspan=3)
        self.btn_ok.config(width=25)

        self.master.mainloop()

    def set_variables(self):
        """Set variables from GUI.
        """
        self.par_folder = self.entry_folder.get()
        self.par_file = self.entry_file.get()
        self.par_bool = self.par_b

    def set_gui_variables(self):
        """Set GUI variables.
        """

    def set_folder(self):
        """Set the folder by filedialog.
        """

        self.par_folder = filedialog.askdirectory()
        self.entry_folder.delete(0, END)
        self.entry_folder.insert(0, self.par_folder)
        LOGGER.debug('Folder: %s', self.par_folder)
        self.folder_created_by_dialog = True

    def set_file(self):
        """Set the file by filedialog.
        """

        self.par_file = filedialog.askopenfilename()
        self.entry_file.delete(0, END)
        self.entry_file.insert(0, self.par_file)
        LOGGER.debug('File: %s', self.par_file)
        self.file_created_by_dialog = True

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
        self.create_gui()

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
