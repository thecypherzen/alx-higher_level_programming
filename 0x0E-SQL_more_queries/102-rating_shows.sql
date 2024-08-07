-- A script that lists all shows from hbtn_0d_tvshows_rate by their rating
--
-- Constraints
--
-- Each record should display: tv_shows.title - rating sum
-- Results must be sorted in descending order by the rating
-- Can only use one SELECT statement

SELECT tv_shows.title, SUM(tv_show_ratings.rate) AS 'rating'
FROM tv_shows
	 JOIN tv_show_ratings
	 ON tv_shows.id = tv_show_ratings.show_id
GROUP BY 1
ORDER BY 2 DESC;
