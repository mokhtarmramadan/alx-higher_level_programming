#!/usr/bin/python3
""" lists all cities from the database hbtn_0e_4_usa """
import MySQLdb
from sys import argv


if __name__ == '__main__':
    db = MySQLdb.connect(host="localhost", user=argv[1],
                         passwd=argv[2], db=argv[3], port=3306)
    cur = db.cursor()
    state = argv[4]
    cur.execute("SELECT cities.name FROM states\
                join cities on states.id = cities.state_id\
                where states.name = %s", (state,))
    entries = cur.fetchall()
    for i in range(len(entries)):
        if i == len(entries) - 1:
            print(f'{entries[i][0]}', end='')
        else:
            print(f'{entries[i][0]}, ', end='')

    print()
    cur.close()
    db.close()
