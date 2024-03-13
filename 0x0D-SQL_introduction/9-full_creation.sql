-- A script that creates the table second_table in the database
-- + and inserts multiple rows into it.
-- If second_table alreay exists, code should not fail
-- Records for each row are provided on the intranet as seen below

CREATE TABLE IF NOT EXISTS second_table
(
	id INT,
	name VARCHAR(256),
	score INT
);

-- Insert records
INSERT INTO
	   second_table(id, name, score)
	   VALUES (1, 'John', 10)
	   ,(2, 'Alex', 3)
	   ,(3, 'Bob', 14)
	   ,(4, 'George', 8);
