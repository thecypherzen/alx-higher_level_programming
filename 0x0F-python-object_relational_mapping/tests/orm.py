#!/usr/bin/python3

import MySQLdb as msdb

conn = msdb.connect(
    host='localhost',
    user='root',
    passwd='RootUser@941')

cursor = conn.cursor()
res = cursor.execute("SHOW DATABASES")
for db in cursor:
    print(db, cursor.r)

cursor.close()
conn.close()
