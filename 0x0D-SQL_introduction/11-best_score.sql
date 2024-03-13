-- A script that lists all records with a score >= 10 of the table
-- + second_table of the database.
-- Results should display both the score and the name in the order score, name.
-- Records should be ordered by score (top first)

SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC;
