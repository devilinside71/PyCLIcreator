# -*- coding: utf-8 -*-
"""
Text formatter class
"""

import logging
import sys

__author__ = 'Laszlo Tamas'
__copyright__ = 'Copyright 2027, Laszlo Tamas'
__license__ = 'MIT'
__version__ = '0.0.1'
__maintainer__ = 'Laszlo Tamas'
__email__ = 'noreply@gmail.com'
__status__ = 'Initial'

LOGGER = logging.getLogger('textformatter')
# set level for file handling (NOTSET>DEBUG>INFO>WARNING>ERROR>CRITICAL)
LOGGER.setLevel(logging.DEBUG)

# create file handler which logs even debug messages
LOGGER_FH = logging.FileHandler('textformatter.log')

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


class TextFormatter():
    """Main class.

    """

    def __init__(self):
        self.string_to_format = ''

    def get_normalized_name(self, name_str, mode):
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


if __name__ == '__main__':
    LOGGER.debug('Start program')
    PROG = TextFormatter()
    LOGGER.debug(PROG.get_normalized_name('Árvíztűrő tükörfúrógép', 'normal'))
    LOGGER.debug(PROG.get_normalized_name(
        'Árvíztűrő tükörfúrógép', 'filename'))
    LOGGER.debug(PROG.get_normalized_name(
        'Árvíztűrő tükörfúrógép', 'classname'))
    LOGGER.debug('Exit program')
    sys.exit()
