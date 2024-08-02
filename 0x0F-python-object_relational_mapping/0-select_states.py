#!/usr/bin/python3
"""The module on MySQLdb"""
import MySQLdb
import sys
if __name__ == "__main__":
    args = sys.argv
    user = args[1]
    password = args[2]
    database = args[3]

    db = MySQLdb.connect(host='localhost', user=user,
            password=password, port=3306, database=database)

    dcur = db.cursor()
    dbquery = """SELECT * FROM states ORDER BY id ASC"""
    dcur.execute(dbquery)
    dbresult = dcur.fetchall()
    for x in dbresult:
        print(x)

    dcur.close()
    db.close()
