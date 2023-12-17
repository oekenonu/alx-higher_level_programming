#!/usr/bin/python3
"""Get city by states from db"""
import MySQLdb
import sys


if __name__ == "__main__":

    db = MySQLdb.connect(host='localhost', user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = db.cursor()
    query = """SELECT c.name FROM cities c
               JOIN states s ON s.id=c.state_id
               where s.name = %s ORDER BY c.id ASC"""
    cur.execute(query, (sys.argv[4],))
    rows = cur.fetchall()
    for i, data in enumerate(rows):
        print(data[0], end=", " if i < len(rows) - 1 else "")
    print()
    cur.close()
    db.close()
