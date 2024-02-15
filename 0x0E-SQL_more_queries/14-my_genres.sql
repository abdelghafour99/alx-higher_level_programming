-- That script uses the hbtn_0d_tvshows database to lists all genres of the show Dexter
SELECT tg.'name'
  FROM 'tv_genres' AS tg
       INNER JOIN 'tv_show_genres' AS tvg
       ON tg.'id' = tvg.'genre_id'

       INNER JOIN `tv_shows` AS tvs
       ON tvs.`id` = svs.`show_id`
       WHERE tvs.`title` = "Dexter"
 ORDER BY tg.'name'
