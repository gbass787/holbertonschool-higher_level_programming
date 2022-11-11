#!/usr/bin/python3
'''Script that takes in the name of a state as an argument and lists all cities of that state'''
import sys
import MySQLdb

if __name__ == "__main__":
    user = sys.argv[1]
    passwd = sys.argv[2]
    database = sys.argv[3]
    states = sys.argv[4]
    db = MySQLdb.connect('localhost', user, passwd, database, 3306)
    c = db.cursor()
    c.execute("""SELECT name FROM cities
            WHERE state_id = (SELECT id FROM states
            WHERE name='{}')
            ORDER BY id""".format(states))
    rows = c.fetchall()
    cities = list()
    for row in rows:
        cities.append(*row)
    print(', '.join(cities))
    db.close()