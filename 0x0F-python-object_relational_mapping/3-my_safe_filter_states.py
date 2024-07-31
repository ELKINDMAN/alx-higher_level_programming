#!/usr/bin/python3
"""MySQL module"""
import MySQLdb
import sys
if __name__ == "__main__":
    args = sys.argv
    user = args[1]
    password = args[2]
    database = args[3]
    user_arg = arg[4]

    db = MySQLdb.connect(host='localhost', user=user, password=password,
                            port=3306, database=database)
    dbcur = db.cursor()
    dbquery = 'SELECT * FROM states WHERE BINARY name = %s ORDER BY id'
    dbcur.execute(query, (user_srg,))
    dbresult = dbcur.fetchall()
    for x in dbresult:
        print(x)

    dbcur.close()
    db.close()
