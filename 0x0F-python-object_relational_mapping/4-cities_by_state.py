#!/usr/bin/python3

""" A script that lists all cities from the database hbtn_0e_4_usa

- takes 3 arguments: mysql username, mysql password, and database name
- uses the module MySQLdb (import MySQLdb)
- connects to a MySQL server running on localhost at port 3306
- results sorted in ascending order by cities.id
- can only use execute statemen once
- results displayed in the form:
     (1, 'San Francisco', 'California')
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
    SELECT cities.id,
        cities.name, states.name
    FROM cities
        JOIN states
        ON cities.state_id = states.id
    ORDER BY cities.id
    """

    cursor.execute(query)
    res = cursor.fetchall()
    for row in res:
        print(row)

    cursor.close()
    conn.close()
