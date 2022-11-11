#!/usr/bin/python3
'''Script that lists all states from the database hbtn_0e_0_usa'''
import sys
import MySQLdb

if __name__ == "__main__":
    user = sys.argv[1]
    passwd = sys.argv[2]
    database = sys.argv[3]

    db = MySQLdb.connect('localhost', user, passwd, database, 3306)

    try:
        c = db.cursor()
        c.execute("SELECT * FROM states ORDER BY id ASC")
        rows = c.fetchall()
        for row in rows:
            print(row)
    except:
        db.rollback()

    db.close()