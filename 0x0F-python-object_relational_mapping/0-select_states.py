""" Module to get all States from hbtn_0e_0_usa database"""
import MySQLdb

db = MySQLdb.connect(user='root', passwd='root', db='hbtn_0e_0_usa')
cur = db.cursor()

cur.execute("SELECT * FROM states ORDER BY id ASC")
for data in cur.fetchall():
    print(data)
