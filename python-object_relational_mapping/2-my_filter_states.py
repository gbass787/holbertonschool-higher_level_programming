#!/usr/bin/python3
'''Script that takes in an argument and displays all values in the states table'''
import sys
import MySQLdb

if __name__ == "__main__":
    user = sys.argv[1]
    passwd = sys.argv[2]
    database = sys.argv[3]
    state = sys.argv[4]
    db = MySQLdb.connect('localhost', user, passwd, database, 3306)
    c = db.cursor()
    c.execute("""SELECT * FROM states WHERE BINARY name='{}'
                ORDER BY id ASC""".format(state))
    rows = c.fetchall()
    for row in rows:
        print(row)
    db.close()