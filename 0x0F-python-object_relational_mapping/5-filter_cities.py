#!/usr/bin/python3
"""My module for MySQLdb"""

import MySQLdb
import sys

if __name__ == "__main__":
    myag = sys.argv
    username = myag[1]
    password = myag[2]
    database = myag[3]
    state_name = myag[4]

    my_db = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=username,
            password=password,
            database=database
            )

    db_cur = my_db.cursor()

    db_query = """SELECT cities.name FROM cities
        INNER JOIN states ON cities.state_id = states.id
        WHERE states.name LIKE %s
        ORDER BY states.id"""
    db_cur.execute(query, (state_name))
    result = db_cur.fetchall()
    val = ''
    for x in result:
        val += f'{x[0]}, '
    val = val.rstrip(', ')
    print(val)
    db_cur.close()
    my_db.close()
