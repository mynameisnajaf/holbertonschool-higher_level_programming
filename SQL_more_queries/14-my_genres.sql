-- uses the hbtn_0d_tvshows database to lists all genres of the show Dexter.
SELECT g.name AS name
FROM tv_genres g
JOIN tv_show_genres sg ON g.id = sg.genre_id
JOIN tv_shows s ON s.id = sg.tv_show_id
WHERE s.title = 'Dexter'
ORDER BY name;
