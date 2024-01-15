#!/usr/bin/python3
""" lists all cities from the database hbtn_0e_4_usa """
import MySQLdb
from sys import argv


if __name__ == '__main__':
    db = MySQLdb.connect(host="localhost", user=argv[1],
                         passwd=argv[2], db=argv[3], port=3306)
    cur = db.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name FROM states\
                join cities on states.id = cities.state_id")
    entries = cur.fetchall()
    for entry in entries:
        print(entry)
    cur.close()
    db.close()
