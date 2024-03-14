-- A script that lists all shows, and all genres linked to that show, from the
-- + database hbtn_0d_tvshows.
--
-- CONSTRAINTS
--
-- If a show doesn’t have a genre, display NULL in the genre column
-- Each record should display: tv_shows.title - tv_genres.name
-- Results must be sorted in ascending order by the show title and genre name
-- Can only use one SELECT statement

SELECT tv_shows.title, tv_genres.name
FROM tv_shows
	 LEFT JOIN tv_show_genres
	 	  ON tv_shows.id = tv_show_genres.show_id
	 LEFT JOIN tv_genres
	 	  ON tv_genres.id = tv_show_genres.genre_id
ORDER BY 1, 2;
