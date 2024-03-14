-- A script that uses the hbtn_0d_tvshows database to list all genres not
-- + linked to the show Dexter
--
-- CONSTRAINTS
--
-- The tv_shows table contains only one record where title = Dexter
-- + (but the id can be different)
-- Each record should display: tv_genres.name
-- Results must be sorted in ascending order by the genre name
-- Can only use a maximum of two SELECT statement

SELECT DISTINCT  tv_genres.name
FROM tv_genres
	 LEFT JOIN tv_show_genres
	 	 ON tv_genres.id = tv_show_genres.genre_id
	 LEFT JOIN tv_shows
	 	 ON tv_shows.id = tv_show_genres.show_id
WHERE tv_shows.title != 'Dexter' &&
	  tv_genres.id NOT IN (SELECT tv_show_genres.genre_id
	  			   FROM tv_shows
				   		JOIN tv_show_genres
				   			 ON tv_shows.id = tv_show_genres.show_id
						JOIN tv_genres
							 ON tv_genres.id = tv_show_genres.genre_id
					WHERE tv_shows.title = 'Dexter'
					)
ORDER BY 1;
