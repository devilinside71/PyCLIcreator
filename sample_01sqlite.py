# -*- coding: utf-8 -*-
"""
__DESCRIPTION__
"""

import sqlite3
import argparse
import errno
import logging
import os
import sys

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
LOGGER_FH = logging.FileHandler('__PROJECTNAMELCASE__.log')

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
    """ Sample SQLite3 class.
    """

    def __init__(self):
        self.args = self.parse_arguments()
        # __INITARG1__
        # __INITARG2__
        # __INITARG3__
        # __INITARG4__
        # __INITARG5__
        self.database = "C:\\sqlite\\db\\pythonsqlite.db"
        self.sql_create_projects_table = """ CREATE TABLE IF NOT EXISTS projects (
                                            id integer PRIMARY KEY,
                                            name text NOT NULL,
                                            begin_date text,
                                            end_date text
                                        ); """

        self.sql_create_tasks_table = """CREATE TABLE IF NOT EXISTS tasks (
                                        id integer PRIMARY KEY,
                                        name text NOT NULL,
                                        priority integer,
                                        status_id integer NOT NULL,
                                        project_id integer NOT NULL,
                                        begin_date text NOT NULL,
                                        end_date text NOT NULL,
                                        FOREIGN KEY (project_id) REFERENCES projects (id)
                                    );"""
        self.connection = None

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
        parser.add_argument('-db', '--database', help='database path')
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
        if self.args.database is not None:
            self.database = self.args.database

        # __EXECLOGARG1__
        # __EXECLOGARG2__
        # __EXECLOGARG3__
        # __EXECLOGARG4__
        # __EXECLOGARG5__
        LOGGER.debug('Database path: %s', self.database)

    def create_connection(self, db_file):
        """ Create a database connection to the SQLite database

        Arguments:
            db_file {sqlite3 db} -- database file name

        Returns:
            various -- database connection or None
        """

        try:
            conn = sqlite3.connect(db_file)
            LOGGER.debug('SQLite version: %s', sqlite3.version)
            return conn
        except sqlite3.Error as sql_err:
            LOGGER.error(sql_err)
        return None

    def create_table(self, conn, create_table_sql):
        """ Create a table from the create_table_sql statement.

        Arguments:
            conn {obj} -- Connection object
            create_table_sql {statement} -- a CREATE TABLE statement
        """

        try:
            sql_cursor = conn.cursor()
            sql_cursor.execute(create_table_sql)
        except sqlite3.Error as sql_err:
            LOGGER.error(sql_err)

    def create_project_data(self, conn, project_data):
        """
        Create a new project into the projects table
        :param conn:
        :param project:
        :return: project id
        """
        sql = ''' INSERT INTO projects(name,begin_date,end_date)
                VALUES(?,?,?) '''
        sql_cursor = conn.cursor()
        sql_cursor.execute(sql, project_data)
        return sql_cursor.lastrowid

    def create_task_data(self, conn, task_data):
        """
        Create a new task
        :param conn:
        :param task:
        :return:
        """

        sql = ''' INSERT INTO tasks(name,priority,status_id,project_id,begin_date,end_date)
                VALUES(?,?,?,?,?,?) '''
        sql_cursor = conn.cursor()
        sql_cursor.execute(sql, task_data)
        return sql_cursor.lastrowid

    # create a database connection
    def execute_sql_creation(self, close_connection=False):
        """ Create database and tables.
        """

        self.connection = self.create_connection(self.database)
        if self.connection is not None:
            # create projects table
            self.create_table(self.connection, self.sql_create_projects_table)
            # create tasks table
            self.create_table(self.connection, self.sql_create_tasks_table)
            if close_connection:
                self.connection.close()
        else:
            LOGGER.error('Error! Cannot create the database connection.')

    def add_sample_data(self):
        """ Add sample data.
        """

        with self.connection:
            # create a new project
            project = ('Cool App with SQLite & Python',
                       '2015-01-01', '2015-01-30')
            project_id = self.create_project_data(self.connection, project)

            # tasks
            task_1 = ('Analyze the requirements of the app', 1,
                      1, project_id, '2015-01-01', '2015-01-02')
            task_2 = ('Confirm with user about the top requirements',
                      1, 1, project_id, '2015-01-03', '2015-01-05')

            # create tasks
            self.create_task_data(self.connection, task_1)
            self.create_task_data(self.connection, task_2)

    @classmethod
    def update_task(cls, conn, task):
        """
        update priority, begin_date, and end date of a task
        :param conn:
        :param task:
        :return: project id
        """
        sql = ''' UPDATE tasks
                SET priority = ? ,
                    begin_date = ? ,
                    end_date = ?
                WHERE id = ?'''
        sql_cursor = conn.cursor()
        sql_cursor.execute(sql, task)

    def update_task_data(self):
        """ Update record.
        """

        self.update_task(self.connection, (2, '2015-01-04', '2015-01-06', 2))

    @classmethod
    def delete_task(cls, conn, task):
        """
        Update priority, begin_date, and end date of a task.
        :param conn:
        :param task:
        :return: project id
        """
        sql = 'DELETE FROM tasks WHERE id=?'
        sql_cursor = conn.cursor()
        sql_cursor.execute(sql, task)

    @classmethod
    def delete_all_tasks(cls, conn):
        """
        Delete all rows in the tasks table.
        :param conn: Connection to the SQLite database
        :return:
        """
        sql = 'DELETE FROM tasks'
        sql_cursor = conn.cursor()
        sql_cursor.execute(sql)

    def delete_task_data(self):
        """ Delete record.
        """

        self.delete_task(self.connection, 2)

    def delete_all_task_data(self):
        """ Delete all records.
        """

        self.delete_all_tasks(self.connection)

    @classmethod
    def select_all_tasks(cls, conn):
        """
        Query all rows in the tasks table
        :param conn: the Connection object
        :return:
        """
        cur = conn.cursor()
        cur.execute("SELECT * FROM tasks")

        rows = cur.fetchall()

        for row in rows:
            LOGGER.debug(row)

    @classmethod
    def select_task_by_priority(cls, conn, priority):
        """
        Query tasks by priority
        :param conn: the Connection object
        :param priority:
        :return:
        """
        cur = conn.cursor()
        cur.execute("SELECT * FROM tasks WHERE priority=?", (priority,))

        rows = cur.fetchall()

        for row in rows:
            LOGGER.debug(row)

    def select_all_tasks_data(self):
        """ Select all data.
        """

        self.select_all_tasks(self.connection)

    def select_all_tasks_data_by_priority(self):
        """ Select all data by priority.
        """

        self.select_task_by_priority(self.connection, 1)

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
    PROG.execute_sql_creation()
    PROG.add_sample_data()
    PROG.update_task_data()
    LOGGER.debug('Exit program')
    sys.exit()
