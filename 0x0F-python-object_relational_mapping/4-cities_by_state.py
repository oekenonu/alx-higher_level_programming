#!/usr/bin/python3
"""Get city by states from db"""
import MySQLdb
import sys


if __name__ == "__main__":

    db = MySQLdb.connect(host='localhost', user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = db.cursor()
    query = """SELECT c.id, c.name, s.name FROM cities c
               JOIN states s ON s.id=c.state_id ORDER BY c.id ASC"""
    cur.execute(query)
    rows = cur.fetchall()
    for data in rows:
        print(data)
    cur.close()
    db.close()
