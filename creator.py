#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Todo
# Character input qustion
# Process questions method
# Questions COMMON
# Project name, type


import sys
import re
import os
from pathlib import Path

# PROJECT_TYPES = ["Javascript", "Python3 CLI"]

PROJECT_TYPES = [
    ["Javascript",
     ["javascript_samples",
      [
          ["test.html", ""],
          ["test.js", "js"]]]
     ],
    ["Python3", ["python3_samples"]]
]


PYTHON3_TYPES = ["Standard", "With SQLite3"]


class Creator():
    """Main class
    """

    def __init__(self):
        """Init
        """
        self.q_common = []
        self.project_file_name = ""
        self.project_folder = ""
        self.project_file = ""
        self.project_class_name = ""

    def execute_program(self):
        """Start program
        """
        print("Start")
        self.input_common()

        self.process_questions()

    def input_common(self):
        """Enter common parameters
        """
        print("Project type:")
        project_type_counter = 0
        for project_type in PROJECT_TYPES:
            project_type_counter = project_type_counter+1
            print(str(project_type_counter)+"- "+project_type[0])
        print("Any other - Quit")
        in_text = input()
        print(len(PROJECT_TYPES))
        if int(in_text) < 1 or int(in_text) > len(PROJECT_TYPES):
            sys.exit()
        self.q_common.append(PROJECT_TYPES[int(in_text)-1][0])
        print("Before creating a project, create it on GitHub\nwith the same name (CamelCase)!!!")
        in_text = input("Project name:\n")
        if in_text.strip == '':
            sys.exit()
        self.q_common.append(in_text)

    def process_questions(self):
        """Process question to create new project
        """
        print("Projext type: " + self.q_common[0])
        print("Project name: " + self.q_common[1])
        self.project_class_name = self.q_common[1]
        self.project_file_name = self.camelcase_to_snakcase(self.q_common[1])+".py"
        self.project_folder = os.path.join(self.get_home_dir(), "dev", self.project_class_name)
        self.project_file = os.path.join(self.get_home_dir(), "dev", self.project_class_name, self.project_file_name)
        # Create project folder
        self.create_folder(self.project_folder)

        # Main filename
        print(self.project_file)

        # Current dir
        print(os.getcwd())

        # Sample files
        # sample_dir = self.get_sapmle_dir(self.q_common[0])
        # print("Sample dir: "+sample_dir)
        for proj_type in PROJECT_TYPES:
            if proj_type[0] == self.q_common[0]:
                print("Sample dir: "+os.path.join(os.getcwd(), proj_type[1][0]))

    def get_sapmle_dir(self, project_type):
        for proj_type in PROJECT_TYPES:
            if proj_type[0] == project_type:
                return os.path.join(os.getcwd(), proj_type[1][0])

    def camelcase_to_snakcase(self, input_str):
        return re.sub(r'(?<!^)(?=[A-Z])', '_', input_str).lower()

    def snakecase_to_camelcase(self, input_str):
        return ''.join(x.capitalize() or '_' for x in input_str.split('_'))

    def get_home_dir(self):
        return str(Path.home())

    @ staticmethod
    def create_folder(folder_name):
        """Create folder recirsively for new project.

        Arguments:
            folder_name {str} -- target folder name

        Returns:
            bool -- folder created succesfuly
        """
        ret = False
        # Check if folder exists
        folder_exists = os.path.isdir(folder_name)
        if folder_exists:
            pass
        else:
            # create folder
            try:
                os.makedirs(folder_name)
                ret = True
            except:
                ret = False
        return ret


if __name__ == '__main__':
    PROG = Creator()
    PROG.execute_program()
    sys.exit()
