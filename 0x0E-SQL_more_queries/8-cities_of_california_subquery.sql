-- A script that lists all the cities of California that can be found in the
-- database hbtn_0d_usa
-- Not allowed to use JOIN keyword.

SELECT * FROM cities
WHERE state_id = (
	  SELECT id FROM states WHERE name='California'
);
