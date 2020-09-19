#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Todo
# Character input qustion
# Process questions method
# Questions COMMON
# Project name, type


import sys
import re
from shutil import copyfile
import os
from pathlib import Path

# PROJECT_TYPES = ["Javascript", "Python3 CLI"]


# All "sample" will be repleced by project filename
PROJECT_TYPES = [
    ["Javascript",
     ["javascript_samples",
      [
          ["sample.html", "", "index.html", True],
          ["sample.js", "js", "sample.js", True],
          ["sample.css", "css", "sample.css", True],
          ["bootstrap.css.map", "css", "bootstrap.css.map", False],
          ["bootstrap.css", "css", "bootstrap.css", False],
          ["bootstrap.bundle.js.map", "js", "bootstrap.bundle.js.map", False],
          ["bootstrap.bundle.js", "js", "bootstrap.bundle.js", False],
          ["jquery-ui.min.js", "js", "jquery-ui.min.js", False],
          #   ["jquery-ui.min.map", "js", "jquery-ui.min.map", False],
          ["jquery-3.5.1.min.js", "js", "jquery-3.5.1.min.js", False],
          ["jquery-3.5.1.min.map", "js", "jquery-3.5.1.min.map", False],
          ["eslintrc.json", "", ".eslintrc.json", True],
          ["package.json", "", "package.json", True],
          ["README.md", "", "README.md", True],

      ]]
     ],
    ["Python3",
     ["python3_samples",
      [
          ["sample.py", "", "sample.py", True],
          ["sample_unittest.py", "", "sample_unittest.py", True],
          ["README.md", "", "README.md", True],
      ]]
     ],
]


PYTHON3_TYPES = ["Standard", "With SQLite3"]


class Creator():
    """Main class
    """

    def __init__(self):
        """Init
        """
        # self.q_common = []
        self.project_type = ""
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
        self.project_type = PROJECT_TYPES[int(in_text)-1][0]
        # self.q_common.append(PROJECT_TYPES[int(in_text)-1][0])
        print("Before creating a project, create it on GitHub\nwith the same name (CamelCase)!!!")
        in_text = input("Project name:\n")
        if in_text.strip == '':
            sys.exit()
        self.project_class_name = in_text
        # self.q_common.append(in_text)

    def process_questions(self):
        """Process question to create new project
        """
        print("Projext type: " + self.project_type)
        print("Project name: " + self.project_class_name)
        self.project_file_name = self.camelcase_to_snakcase(self.project_class_name)
        self.project_folder = os.path.join(self.get_home_dir(), "dev", self.project_class_name)
        self.project_file = os.path.join(
            self.get_home_dir(),
            "dev", self.project_class_name, self.project_file_name, ".py")
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
            if proj_type[0] == self.project_type:
                sample_dir = os.path.join(os.getcwd(), proj_type[1][0])
                print("Sample dir: "+sample_dir)
                for proj_files in proj_type[1][1]:
                    source_file = os.path.join(sample_dir, proj_files[0])
                    temp_file_name = proj_files[2].replace("sample", self.project_file_name)
                    target_file = os.path.join(
                        self.project_folder, proj_files[1], temp_file_name)
                    print("Copy "+source_file+" to "+target_file + " > Change inner text: "+str(proj_files[3]))
                    self.create_folder(os.path.join(self.project_folder, proj_files[1]))
                    copyfile(source_file, target_file)
                    if proj_files[3]:
                        self.replace_in_file(target_file)

    def replace_in_file(self, file_name):
        data = ""
        with open(file_name, 'r') as myfile:
            data = myfile.read()
            data = data.replace("PROJECT_NAME", self.project_class_name)
            data = data.replace("PROJECT_SNAKE", self.project_file_name)

        # print(data)
        text_file = open(file_name, 'w', encoding='utf-8')
        text_file.write(data)
        text_file.close()

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
