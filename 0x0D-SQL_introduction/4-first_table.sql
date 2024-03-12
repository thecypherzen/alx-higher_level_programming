-- Creates a table called first_table in the current database in your MySQL \
-- +server. It doesn't fail if table already exists
-- use of `SHOW` or `SELECT` not allowed

CREATE TABLE IF NOT EXISTS first_table
(
	id INT,
	name VARCHAR(256)
);
