#!/usr/bin/python3
"""Get all States stating with N from hbtn_0e_0_usa database"""


if __name__ == "__main__":
    import MySQLdb
    import sys

    db = MySQLdb.connect(host='localhost', user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = db.cursor()

    cur.execute("SELECT * FROM states where name LIKE 'N%'")
    rows = cur.fetchall()
    for data in rows:
        print(data)
    cur.close()
    db.close()
