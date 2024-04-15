#!/usr/bin/python3

""" A script that lists all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa

- takes 3 arguments: mysql username, mysql password and database name
- uses the module MySQLdb (import MySQLdb)
- connects to a MySQL server running on localhost at port 3306
- resulst sorted in ascending order by states.id
- results displayed in the form:
     (4, 'New York')
     (5, 'Nevada')
- code should not be executed when imported
"""

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
    query = """
    SELECT id, name
        FROM states
    WHERE name COLLATE utf8mb4_bin like 'N%'
    ORDER BY states.id
    """
    cursor.execute(query)

    res = cursor.fetchall()
    for row in res:
        print(row)

    cursor.close()
    conn.close()
