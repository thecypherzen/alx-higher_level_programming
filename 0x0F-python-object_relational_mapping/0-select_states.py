#!/usr/bin/python3

""" A script that lists all states in a Database """

if __name__ == "__main__":
    import MySQLdb as msdb
    import sys

    conn = msdb.connect(
        host='localhost',
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    cursor = conn.cursor()
    cursor.execute("SELECT * FROM states ORDER BY states.id")

    res = cursor.fetchall()
    for row in res:
        print(row)

    cursor.close()
    conn.close()
