#!/usr/bin/python3
'''Script that lists all cities from the database hbtn_0e_4_usa'''
import sys
import MySQLdb

if __name__ == "__main__":
    user = sys.argv[1]
    passwd = sys.argv[2]
    database = sys.argv[3]
    db = MySQLdb.connect('localhost', user, passwd, database, 3306)
    c = db.cursor()
    c.execute("""SELECT cities.id, cities.name, states.name
            FROM cities JOIN states
            ON states.id = cities.state_id
            ORDER BY cities.id""")
    rows = c.fetchall()
    for row in rows:
        print(row)
    db.close()