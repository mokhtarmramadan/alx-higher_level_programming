#!/usr/bin/python3
"""  takes in an argument and displays all values in the states table """
import MySQLdb
from sys import argv

if __name__ == '__main__':

    db = MySQLdb.connect(host="localhost", user=argv[1],
                         passwd=argv[2], db=argv[3], port=3306)
    cur = db.cursor()
    state = argv[4]
    cur.execute("SELECT * FROM states WHERE name='{}'".format(state))
    entries = cur.fetchall()
    for entry in entries:
        print(entry)
    cur.close()
    db.close()
