-- Import the database dump from hbtn_0d_tvshows to your MySQL server: download
SELECT cities.id, cities.name, states.name
FROM cities, states
WHERE cities.state_id = states.id
ORDER BY cities.id ASC;
