#!/usr/bin/python3
'''Script that takes in arguments and displays all values in the states table of hbtn_0e_0_usa where name matches the argument'''
import sys
import MySQLdb

if __name__ == "__main__":
    user = sys.argv[1]
    passwd = sys.argv[2]
    database = sys.argv[3]
    state = sys.argv[4]
    db = MySQLdb.connect('localhost', user, passwd, database, 3306)
    c = db.cursor()
    c.execute("""SELECT * FROM states WHERE name = %(state)s
                ORDER BY id ASC""", {'state': state})
    rows = c.fetchall()
    for row in rows:
        print(row)
    db.close()