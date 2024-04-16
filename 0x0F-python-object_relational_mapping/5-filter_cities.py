#!/usr/bin/python3

""" A script that takes in the name of a state as an argument and lists all
cities of that state, using the database hbtn_0e_4_usa in an injection-free
manner.

- takes 4 arguments: mysql username, mysql password, database name,
    and state name
- uses the module MySQLdb (import MySQLdb)
- connects to a MySQL server running on localhost at port 3306
- results sorted in ascending order by cities.id
- can only use execute() method once
- results displayed in the form:
     Dallas, Houston, Austin
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
    SELECT cities.name
    FROM cities
        JOIN states
        ON cities.state_id = states.id
    WHERE states.name COLLATE utf8mb4_bin = %s
    ORDER BY cities.id
    """

    cursor.execute(query, (sys.argv[4],))
    res = cursor.fetchall()
    res = ", ".join(str(item[0]) for item in res)
    print(res)

    cursor.close()
    conn.close()
