#!/usr/bin/python3
"""Module for the MySQLdb"""
import MySQLdb
import sys
if __name__ == "__main__":
    args = sys.argv
    user = args[1]
    password = args[2]
    database = args[3]

    db = MySQLdb.connect(host='localhost', user=user,
            password=password, port=3306, database=database)

    dbcur = db.cursor()
    dbquery = """SELECT * FROM states
                WHERE BINARY name LIKE 'N%'"""
    dbcur.execute(dbquery)
    dbresult = dbcur.fetchall()
    for x in dbresult:
        print(x)

    dbcur.close()
    db.close()
