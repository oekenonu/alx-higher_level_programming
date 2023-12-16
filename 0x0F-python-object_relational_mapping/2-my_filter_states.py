#!/usr/bin/python3
"""Get state passed as arg"""
import MySQLdb
import sys


if __name__ == "__main__":

    db = MySQLdb.connect(host='localhost', user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = db.cursor()
    query = "SELECT * FROM states where name = '{0}'".format(sys.argv[4])
    cur.execute(query)
    rows = cur.fetchall()
    for data in rows:
        print(data)
    cur.close()
    db.close()
