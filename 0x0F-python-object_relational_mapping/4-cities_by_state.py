#!/usr/bin/python3
"""My module for MySQLdb"""

import MySQLdb
import sys

if __name__ == "__main__":
    myarg = sys.argv
    userName = myarg[1]
    password = myarg[2]
    database = myarg[3]

    db_connect = MySQLdb.connect(
        host='localhost',
        user=userName, 
        password=password,
        database=database,
        port = 3306)

    db_cur = db_connect.cursor()

    db_query = """SELECT cities.id, cities.name, states.name FROM cities
        INNER JOIN states
        WHERE cities.state_id = states.id
        ORDER BY cities.id ASC"""
    db_cur.execute(db_query)
    result = db_cur.fetchall()
    for r in result:
        print(r)

    db_cur.close()
    db_connect()
