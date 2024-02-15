-- That script that lists all shows contained in the database hbtn_0d_tvshows
SELECT tv.'title', ge.'genre_id'
  FROM 'tv_shows' AS tv
        LEFT JOIN 'tv_show_genres' AS ge
	ON tv.'id' = ge.'show_id'
 ORDER BY tv.'title', ge.'genre_id';
