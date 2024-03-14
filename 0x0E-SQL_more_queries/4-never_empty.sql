-- A script that creates the table id_not_null on a MySQL server.
-- id_not_null description: id INT with the default value 1 name VARCHAR(256)
-- If the table id_not_null already exists, the script should not fail

CREATE TABLE IF NOT EXISTS id_not_null
(
	id INT NOT NULL DEFAULT 1,
	name VARCHAR(256)
);
