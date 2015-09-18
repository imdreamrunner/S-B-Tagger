__author__ = "Xinzi Zhou"
__email__ = "imdreamrunner@gmail.com"

import MySQLdb

connection = None


def connect():
    global connection
    connection = MySQLdb.connect(host="localhost",  # your host, usually localhost
                                 user="root",  # your username
                                 passwd="lucky",  # your password
                                 db="wetag")  # name of the data base


def disconnect():
    if connection is not None:
        connection.close()


def get_cursor():
    connection.autocommit(True)
    return connection.cursor()
