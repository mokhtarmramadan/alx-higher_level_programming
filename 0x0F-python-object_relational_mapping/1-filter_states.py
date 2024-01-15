#!/usr/bin/python3
""" Lists all states with a name starting with N"""
import MySQLdb
from sys import argv

if __name__ == '__main__':

    db = MySQLdb.connect(host="localhost", user=argv[1],
                         passwd=argv[2], db=argv[3], port=3306)
    cur = db.cursor()
    cur.execute("SELECT * FROM states")
    entries = cur.fetchall()
    for entry in entries:
        if entry[1].startswith('N'):
            print(entry)
    cur.close()
    db.close()
