# -*- coding: utf-8 -*-
"""
Class to create GUI for PyCLIcreator
"""

import argparse
import logging
import sys
from tkinter import Label, Entry, Button, Checkbutton, W, E, END, Tk, filedialog, BooleanVar


__author__ = 'Laszlo Tamas'
__copyright__ = 'Copyright 2027, Laszlo Tamas'
__license__ = 'GPL'
__version__ = '0.0.1'
__maintainer__ = 'Laszlo Tamas'
__email__ = 'noreply@gmail.com'
__status__ = 'Initial'

LOGGER = logging.getLogger('pycligui')
# set level for file handling (NOTSET>DEBUG>INFO>WARNING>ERROR>CRITICAL)
LOGGER.setLevel(logging.DEBUG)

# create file handler which logs even debug messages
LOGGER_FH = logging.FileHandler('pycligui.log')

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


class PyCLIGUI():
    """Main class.

    """

    def __init__(self):
        self.par_output = ''
        self.folder_created_by_dialog = True
        self.master = Tk()

        self.par_name = ''
        self.par_description = ''
        self.par_author = 'Laszlo Tamas'
        self.par_copyright = '(C) 2027'
        self.par_folder = ''
        self.par_version = '0.0.1'
        # self.par_sqlite = True
        self.par_template = 'sample_01.py'
        self.par_testtemplate = 'sample_01_test.py'
        self.par_notestemplate = 'sample_01_README.md'
        self.par_licence = 'MIT'
        self.par_email = 'noreply@gmail.com'
        self.par_status = 'Initial'
        # self.par_forcegui = False
        # self.par_predefined = ''
        self.par_arg1s = ''
        self.par_arg1l = ''
        self.par_arg1help = ''
        self.par_arg1bool = False
        self.par_arg1b = BooleanVar()

        self.par_arg2s = ''
        self.par_arg2l = ''
        self.par_arg2help = ''
        self.par_arg2bool = False
        self.par_arg2b = BooleanVar()

        self.par_arg3s = ''
        self.par_arg3l = ''
        self.par_arg3help = ''
        self.par_arg3bool = False
        self.par_arg3b = BooleanVar()

        self.par_arg4s = ''
        self.par_arg4l = ''
        self.par_arg4help = ''
        self.par_arg4bool = False
        self.par_arg4b = BooleanVar()

        self.par_arg5s = ''
        self.par_arg5l = ''
        self.par_arg5help = ''
        self.par_arg5bool = False
        self.par_arg5b = BooleanVar()

        self.master.title('Python CLI creator')
        self.entry_folder = Entry(self.master)
        self.entry_name = Entry(self.master)
        self.entry_description = Entry(self.master)
        self.entry_author = Entry(self.master)
        self.entry_copyright = Entry(self.master)
        self.entry_version = Entry(self.master)
        self.entry_template = Entry(self.master)
        self.entry_testtemplate = Entry(self.master)
        self.entry_notestemplate = Entry(self.master)
        self.entry_licence = Entry(self.master)
        self.entry_email = Entry(self.master)
        self.entry_status = Entry(self.master)
        # self.chk_sqlite = Checkbutton(
        #     self.master, text="SQLite", variable=self.par_sqlite)
        self.btn_ok = Button(self.master, text='OK',
                             command=self.set_variables)
        self.btn_cancel = Button(
            self.master, text='Cancel', command=self.master.quit)
        # ARGS
        self.entry_arg1s = Entry(self.master)
        self.entry_arg1l = Entry(self.master)
        self.entry_arg1help = Entry(self.master)
        self.chk_arg1bool = Checkbutton(
            self.master, text="Bool", variable=self.par_arg1b)
        if self.par_arg1bool:
            self.chk_arg1bool.select()
        self.entry_arg2s = Entry(self.master)
        self.entry_arg2l = Entry(self.master)
        self.entry_arg2help = Entry(self.master)
        self.chk_arg2bool = Checkbutton(
            self.master, text="Bool", variable=self.par_arg2b)
        if self.par_arg2bool:
            self.chk_arg2bool.select()
        self.entry_arg3s = Entry(self.master)
        self.entry_arg3l = Entry(self.master)
        self.entry_arg3help = Entry(self.master)
        self.chk_arg3bool = Checkbutton(
            self.master, text="Bool", variable=self.par_arg3b)
        if self.par_arg3bool:
            self.chk_arg3bool.select()
        self.entry_arg4s = Entry(self.master)
        self.entry_arg4l = Entry(self.master)
        self.entry_arg4help = Entry(self.master)
        self.chk_arg4bool = Checkbutton(
            self.master, text="Bool", variable=self.par_arg4b)
        if self.par_arg4bool:
            self.chk_arg4bool.select()
        self.entry_arg5s = Entry(self.master)
        self.entry_arg5l = Entry(self.master)
        self.entry_arg5help = Entry(self.master)
        self.chk_arg5bool = Checkbutton(
            self.master, text="Bool", variable=self.par_arg5b)
        if self.par_arg5bool:
            self.chk_arg5bool.select()

    @staticmethod
    def parse_arguments():
        """Parse arguments.

        Returns:
            parser args -- parser argumnents
        """

        parser = argparse.ArgumentParser()
        parser.add_argument('-o', '--output',
                            help='output file')
        parser.add_argument('-v', '--verbose', action='store_true',
                            help='increase output verbosity')
        return parser.parse_args()

    def execute_program(self):
        """Execute the program by arguments.
        """
        args = self.parse_arguments()
        self.par_output = args.output
        LOGGER.debug('Output: %s', self.par_output)
        self.create_gui()

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

        Label(self.master, text='Project Name').grid(
            row=1, column=0, sticky=E)
        self.entry_name.delete(0, END)
        self.entry_name.insert(0, self.par_name)
        self.entry_name.grid(row=1, column=1, columnspan=3, sticky=W)

        Label(self.master, text='Description').grid(
            row=2, column=0, sticky=E)
        self.entry_description.delete(0, END)
        self.entry_description.insert(0, self.par_description)
        self.entry_description.grid(row=2, column=1, columnspan=3, sticky=W)

        Label(self.master, text='Author').grid(row=3, column=0, sticky=E)
        self.entry_author.delete(0, END)
        self.entry_author.insert(0, self.par_author)
        self.entry_author.grid(row=3, column=1, columnspan=3, sticky=W)

        Label(self.master, text='Copyright').grid(
            row=4, column=0, sticky=E)
        self.entry_copyright.delete(0, END)
        self.entry_copyright.insert(0, self.par_copyright)
        self.entry_copyright.grid(row=4, column=1, columnspan=3, sticky=W)

        Label(self.master, text='Version').grid(row=5, column=0, sticky=E)
        self.entry_version.delete(0, END)
        self.entry_version.insert(0, self.par_version)
        self.entry_version.grid(row=5, column=1, columnspan=3, sticky=W)

        Label(self.master, text='Template').grid(row=6, column=0, sticky=E)
        self.entry_template.delete(0, END)
        self.entry_template.insert(0, self.par_template)
        self.entry_template.grid(row=6, column=1, columnspan=3, sticky=W)
        self.entry_template.config(width=70)
        Button(self.master, text='Browse', command=self.set_templatefile).grid(
            row=6, column=4, sticky=W, pady=4)

        Label(self.master, text='Test template').grid(
            row=7, column=0, sticky=E)
        self.entry_testtemplate.delete(0, END)
        self.entry_testtemplate.insert(0, self.par_testtemplate)
        self.entry_testtemplate.grid(row=7, column=1, columnspan=3, sticky=W)
        self.entry_testtemplate.config(width=70)
        Button(self.master, text='Browse', command=self.set_test_templatefile).grid(
            row=7, column=4, sticky=W, pady=4)

        Label(self.master, text='README template').grid(
            row=8, column=0, sticky=E)
        self.entry_notestemplate.delete(0, END)
        self.entry_notestemplate.insert(0, self.par_notestemplate)
        self.entry_notestemplate.grid(row=8, column=1, columnspan=3, sticky=W)
        self.entry_notestemplate.config(width=70)
        Button(self.master, text='Browse', command=self.set_notes_templatefile).grid(
            row=8, column=4, sticky=W, pady=4)

        Label(self.master, text='Licence').grid(row=9, column=0, sticky=E)
        self.entry_licence.delete(0, END)
        self.entry_licence.insert(0, self.par_licence)
        self.entry_licence.grid(row=9, column=1, columnspan=3, sticky=W)

        Label(self.master, text='Email').grid(row=10, column=0, sticky=E)
        self.entry_email.delete(0, END)
        self.entry_email.insert(0, self.par_email)
        self.entry_email.config(width=25)
        self.entry_email.grid(row=10, column=1, columnspan=3, sticky=W)

        Label(self.master, text='Status').grid(row=11, column=0, sticky=E)
        self.entry_status.delete(0, END)
        self.entry_status.insert(0, self.par_status)
        self.entry_status.grid(row=11, column=1, columnspan=3, sticky=W)

        # self.chk_sqlite.grid(row=12, column=1, sticky=W)
        # ARGS
        Label(self.master, text='ARG1').grid(row=12, column=0, sticky=E)
        self.entry_arg1s.grid(row=12, column=1)
        self.entry_arg1s.config(width=2)
        self.entry_arg1s.delete(0, END)
        self.entry_arg1s.insert(0, self.par_arg1s)
        self.entry_arg1l.grid(row=12, column=2)
        self.entry_arg1l.config(width=12)
        self.entry_arg1l.delete(0, END)
        self.entry_arg1l.insert(0, self.par_arg1l)
        self.entry_arg1help.grid(row=12, column=3)
        self.entry_arg1help.delete(0, END)
        self.entry_arg1help.insert(0, self.par_arg1help)
        self.chk_arg1bool.grid(row=12, column=4)
        Label(self.master, text='ARG2').grid(row=13, column=0, sticky=E)
        self.entry_arg2s.grid(row=13, column=1)
        self.entry_arg2s.config(width=2)
        self.entry_arg2s.delete(0, END)
        self.entry_arg2s.insert(0, self.par_arg2s)
        self.entry_arg2l.grid(row=13, column=2)
        self.entry_arg2l.config(width=12)
        self.entry_arg2l.delete(0, END)
        self.entry_arg2l.insert(0, self.par_arg2l)
        self.entry_arg2help.grid(row=13, column=3)
        self.entry_arg2help.delete(0, END)
        self.entry_arg2help.insert(0, self.par_arg2help)
        self.chk_arg2bool.grid(row=13, column=4)
        Label(self.master, text='ARG3').grid(row=14, column=0, sticky=E)
        self.entry_arg3s.grid(row=14, column=1)
        self.entry_arg3s.config(width=2)
        self.entry_arg3s.delete(0, END)
        self.entry_arg3s.insert(0, self.par_arg3s)
        self.entry_arg3l.grid(row=14, column=2)
        self.entry_arg3l.config(width=12)
        self.entry_arg3l.delete(0, END)
        self.entry_arg3l.insert(0, self.par_arg3l)
        self.entry_arg3help.grid(row=14, column=3)
        self.entry_arg3help.delete(0, END)
        self.entry_arg3help.insert(0, self.par_arg3help)
        self.chk_arg3bool.grid(row=14, column=4)
        Label(self.master, text='ARG4').grid(row=15, column=0, sticky=E)
        self.entry_arg4s.grid(row=15, column=1)
        self.entry_arg4s.config(width=2)
        self.entry_arg4s.delete(0, END)
        self.entry_arg4s.insert(0, self.par_arg4s)
        self.entry_arg4l.grid(row=15, column=2)
        self.entry_arg4l.config(width=12)
        self.entry_arg4l.delete(0, END)
        self.entry_arg4l.insert(0, self.par_arg4l)
        self.entry_arg4help.grid(row=15, column=3)
        self.entry_arg4help.delete(0, END)
        self.entry_arg4help.insert(0, self.par_arg4help)
        self.chk_arg4bool.grid(row=15, column=4)
        Label(self.master, text='ARG5').grid(row=16, column=0, sticky=E)
        self.entry_arg5s.grid(row=16, column=1)
        self.entry_arg5s.config(width=2)
        self.entry_arg5s.delete(0, END)
        self.entry_arg5s.insert(0, self.par_arg5s)
        self.entry_arg5l.grid(row=16, column=2)
        self.entry_arg5l.config(width=12)
        self.entry_arg5l.delete(0, END)
        self.entry_arg5l.insert(0, self.par_arg5l)
        self.entry_arg5help.grid(row=16, column=3)
        self.entry_arg5help.delete(0, END)
        self.entry_arg5help.insert(0, self.par_arg5help)
        self.chk_arg5bool.grid(row=16, column=4)

        self.btn_cancel.grid(row=18, column=0, sticky=W)
        self.btn_ok.grid(row=18, column=2, sticky=W, columnspan=3)
        self.btn_ok.config(width=25)

        self.master.mainloop()

    def set_variables(self):
        """Setup variables from GUI for project creation.
        """

        self.par_folder = self.entry_folder.get()
        self.par_name = self.entry_name.get()
        self.par_description = self.entry_description.get()
        self.par_author = self.entry_author.get()
        self.par_copyright = self.entry_copyright.get()
        self.par_version = self.entry_version.get()
        self.par_template = self.entry_template.get()
        self.par_testtemplate = self.entry_testtemplate.get()
        self.par_notestemplate = self.entry_notestemplate.get()
        self.par_licence = self.entry_licence.get()
        self.par_email = self.entry_email.get()
        self.par_status = self.entry_status.get()

        self.par_arg1s = self.entry_arg1s.get()
        self.par_arg1l = self.entry_arg1l.get()
        self.par_arg1help = self.entry_arg1help.get()
        self.par_arg1bool = self.par_arg1b.get()
        # self.par_arg1bool = False
        self.par_arg2s = self.entry_arg2s.get()
        self.par_arg2l = self.entry_arg2l.get()
        self.par_arg2help = self.entry_arg2help.get()
        self.par_arg2bool = self.par_arg2b.get()
        # self.par_arg2bool = False
        self.par_arg3s = self.entry_arg3s.get()
        self.par_arg3l = self.entry_arg3l.get()
        self.par_arg3help = self.entry_arg3help.get()
        self.par_arg3bool = self.par_arg3b.get()
        # self.par_arg3bool = False
        self.par_arg4s = self.entry_arg4s.get()
        self.par_arg4l = self.entry_arg4l.get()
        self.par_arg4help = self.entry_arg4help.get()
        self.par_arg4bool = self.par_arg4b.get()
        # self.par_arg4bool = False
        self.par_arg5s = self.entry_arg5s.get()
        self.par_arg5l = self.entry_arg5l.get()
        self.par_arg5help = self.entry_arg5help.get()
        self.par_arg5bool = self.par_arg5b.get()
        # self.par_arg5bool = False

        self.master.quit()

    def set_folder(self):
        """Set the project folder by filedialog.
        """

        self.par_folder = filedialog.askdirectory()
        self.entry_folder.delete(0, END)
        self.entry_folder.insert(0, self.par_folder)
        LOGGER.debug('Folder: %s', self.par_folder)
        self.folder_created_by_dialog = True

    def set_templatefile(self):
        """Set the template file by filedialog.
        """

        self.par_template = filedialog.askopenfilename()
        self.entry_template.delete(0, END)
        self.entry_template.insert(0, self.par_template)
        LOGGER.debug('Template: %s', self.par_template)

    def set_test_templatefile(self):
        """Set the testtemplate file by filedialog.
        """

        self.par_testtemplate = filedialog.askopenfilename()
        self.entry_testtemplate.delete(0, END)
        self.entry_testtemplate.insert(0, self.par_testtemplate)
        LOGGER.debug('Test template: %s', self.par_testtemplate)

    def set_notes_templatefile(self):
        """Set the notes template file by filedialog.
        """

        self.par_notestemplate = filedialog.askopenfilename()
        self.entry_notestemplate.delete(0, END)
        self.entry_notestemplate.insert(0, self.par_notestemplate)
        LOGGER.debug('README template: %s', self.par_notestemplate)


if __name__ == '__main__':
    LOGGER.debug('Start program')
    PROG = PyCLIGUI()
    PROG.execute_program()
    LOGGER.debug('Exit program')
    sys.exit()
