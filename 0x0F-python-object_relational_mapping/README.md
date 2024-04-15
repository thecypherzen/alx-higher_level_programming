# Overview #

This directory contains solutions to the **0x0F. Python - Object-relational mapping** project. It intruduces two concepts:<br/>1. The use of mysql in Python, which allows us to execute sql commands and interact with the database from within python, and <br/>2. The use of object relational mappers, which abstracts the use of sql statements and substitutes that with the use of objects, the advantages of which are numerous.

It focuses on the following concepts:
<ol><li>Why Python programming is awesome</li><li>How to connect to a MySQL database from a Python script</li><li>How to `SELECT` rows in a MySQL table from a Python script</li><li>How to `INSERT` rows in a MySQL table from a Python script</li><li>What ORM means</li><li>How to map a Python Class to a MySQL table</li><li>How to create a Python Virtual Environment</li></ol>

### Learning Materials ###
- [Object-relational mappers](https://www.fullstackpython.com/object-relational-mappers-orms.html)
- [mysqlclient/MySQLdb documentation](https://mysqlclient.readthedocs.io/)
- [MySQLdb tutorial](https://www.mikusa.com/python-mysql-docs/index.html)
- [SQLAlchemy tutorial](https://docs.sqlalchemy.org/en/13/orm/tutorial.html)
- [SQLAlchemy](https://docs.sqlalchemy.org/en/13/)
- [mysqlclient/MySQLdb](https://github.com/PyMySQL/mysqlclient)
- [Introduction to SQLAlchemy](https://www.youtube.com/watch?v=woKYyhLCcnU)
- [Flask SQLAlchemy](https://www.youtube.com/playlist?list=PLXmMXHVSvS-BlLA5beNJojJLlpE0PJgCW)
- [10 common stumbling blocks for SQLAlchemy newbies](https://alextechrants.blogspot.com/2013/11/10-common-stumbling-blocks-for.html)
- [Python SQLAlchemy Cheatsheet](https://www.pythonsheets.com/notes/python-sqlalchemy.html)
- [SQLAlchemy ORM Tutorial for Python Developers](https://auth0.com/blog/sqlalchemy-orm-tutorial-for-python-developers/) ***(Warning: This tutorial is with PostgreSQL, but the concept of SQLAlchemy is the same with MySQL)***
- [SQLAlchemy Tutorial](https://overiq.com/sqlalchemy-101/)
- [Python Virtual Environments: A primer](https://realpython.com/python-virtual-environments-a-primer/)

### Project Timeline Details ###
- **Released:** Fri 12 Apr. 2024 - 6am.
- **1st Deadline:** Tue 16 Apr. 2024 - 6am.
- **Duration:** 96 hrs (4 day).
- **Month** 6, **Week** 1, **Day** 1.

## Author ##
- [William Inyam](https://github.com/thecypherzen/)

### Technologies ##
- All Python files written and tested with Python 3.8.10.
- MySQLdb scripts executed with MySQLdb version 2.2.4
- SQLAlchemy scripts executed with SQLAlchemy version 2.0.29
- All shell scripts written in GNU bash 5.0.17(1)-release (x86_64-pc-linux-gnu).
- All python scripts compliant with pycodestyle (version 2.8.*)
- Code tested on Ubuntu 20.04 LTS.

### Prerequisites and Dependencies ###
Successful execution of this project requires the following installations;
#### 1. Python Virtual Environment ####
Necessary to install dependencies specific to project
```
$ sudo apt-get install python3.8-venv
$ python3 -m venv venv
$ source venv/bin/activate
```

#### 2. MySQLdb module  ####
```
$ sudo apt-get install python3-dev
$ sudo apt-get install libmysqlclient-dev
$ sudo apt-get install zlib1g-dev
$ sudo pip3 install mysqlclient
...
$ python3
>>> import MySQLdb
>>> MySQLdb.version_info
(2, 2, 4, 'final', 0)
```

#### 3. SQLAlchemy module ####
```
$ sudo pip3 install SQLAlchemy
...
$ python3
>>> import sqlalchemy
>>> sqlalchemy.__version__
'2.0.29'
```
## File Tree ##
**pending**


## Files ##
Files on the project are task based and are as follows:
| SN | File | Description |
|----|------|-------------|
| 1. |[0-select_states.py](https://github.com/thecypherzen)  | A script that lists all states from the database hbtn_0e_0_usa: <br/><ul><li>The script should take 3 arguments: mysql username, mysql password and database name (no argument validation needed)</li><li>must use the module MySQLdb (import MySQLdb)</li><li>The script should connect to a MySQL server running on localhost at port 3306</li><li>Results must be sorted in ascending order by states.id</li><li>Results must be displayed as below:</br> ```
$./0-select_states.py root root hbtn_0e_0_usa
(1, 'California')<br/>(2, 'Arizona')
(3, 'Texas')</br>(4, 'New York')
(5, 'Nevada')```
</li><li>The code should not be executed when imported</li></ul>|
| 2. | Pending |      |
