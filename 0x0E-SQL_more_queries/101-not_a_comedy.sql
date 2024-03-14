-- A script that lists all shows without the genre Comedy in the database
-- + hbtn_0d_tvshows.
--
-- CONSTRAINTS
--
-- The tv_genres table contains only one record where name = Comedy
-- + (but the id can be different)
-- Each record should display: tv_shows.title
-- Results must be sorted in ascending order by the show title
-- Can use a maximum of two SELECT statements

SELECT DISTINCT tv_shows.title
FROM tv_shows
	 LEFT JOIN tv_show_genres
	 	  ON tv_shows.id = tv_show_genres.show_id
	 LEFT JOIN tv_genres
	 	  ON tv_genres.id = tv_show_genres.genre_id
WHERE tv_genres.id IS NULL OR
	  tv_show_genres.show_id NOT IN(
	   SELECT tv_shows.id
	   FROM tv_shows JOIN tv_show_genres
	   				 	  ON tv_shows.id = tv_show_genres.show_id
					 JOIN tv_genres
					 	  ON tv_genres.id = tv_show_genres.genre_id
	   WHERE tv_genres.name = 'Comedy'
	   )
ORDER BY 1;
