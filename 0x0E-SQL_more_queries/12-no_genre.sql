-- That script lists all shows contained in hbtn_0d_tvshows without a genre linked
SELECT tv.'title', ge.'genre_id'
   FROM 'tv_shows' AS tv
	LEFT JOIN 'tv_show_genres' AS ge
	ON tv.'id' = ge.'show_id'
	WHERE g.`genre_id` IS NULL
   ORDER BY tv.'title', ge.'genre_id';
