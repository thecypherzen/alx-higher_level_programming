-- A script that displays the max temperature of each state
-- + (ordered by State name).
-- Based on temperatures table of task 18

SELECT
	state, MAX(value) AS 'max_temp'
FROM temperatures
GROUP BY 1
ORDER BY 1;
