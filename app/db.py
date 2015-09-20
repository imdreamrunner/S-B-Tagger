__author__ = "Xinzi Zhou"
__email__ = "imdreamrunner@gmail.com"

import MySQLdb
from . import config

connection = None


def connect():
    global connection
    connection = MySQLdb.connect(host=config.get_config('host'),  # your host, usually localhost
                                 user=config.get_config('user'),  # your username
                                 passwd=config.get_config('password'),  # your password
                                 db=config.get_config('database'))  # name of the data base


def disconnect():
    if connection is not None:
        connection.close()


def get_cursor():
    connection.autocommit(True)
    return connection.cursor()
