-- Import the database dump from hbtn_0d_tvshows_rate to your MySQL server: download (same as 102-rating_shows.sql)
SELECT
    tv_genres.name,
    SUM(tv_show_ratings.rate) AS rating
FROM
    tv_genres
JOIN
    tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
JOIN
    tv_show_ratings ON tv_show_genres.show_id = tv_show_ratings.show_id
GROUP BY
    tv_genres.name
ORDER BY
    rating DESC;
