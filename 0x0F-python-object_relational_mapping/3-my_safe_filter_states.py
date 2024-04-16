#!/usr/bin/python3

""" A script that that takes in an argument and displays all values in the
states table of hbtn_0e_0_usa where name matches the argument.
This is done in an injection-safe method.

- takes 4 arguments: mysql username, mysql password,  database name,
    and state name searched.
- uses the module MySQLdb (import MySQLdb)
- connects to a MySQL server running on localhost at port 3306
- resulst sorted in ascending order by states.id
- results displayed in the form:
     (4, 'New York')
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
    WHERE name COLLATE utf8mb4_bin = %s
    ORDER BY states.id
    """
    cursor.execute(query, (sys.argv[4],))

    res = cursor.fetchall()
    for row in res:
        print(row)

    cursor.close()
    conn.close()
