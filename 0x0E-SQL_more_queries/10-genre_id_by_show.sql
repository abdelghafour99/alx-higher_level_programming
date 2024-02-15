-- That script lists all shows contained in hbtn_0d_tvshows that have at least one genre linked
SELECT tv.'title', ge.'genre_id'
   FROM 'tv_shows' AS tv
        INNER JOIN 'tv_show_genres' AS ge
	ON tv.'id' = ge.'show_id'
   ORDER BY tv.'title', ge.'genre_id';
