-- Lists all the cities of California that can be found in the database
SELECT id, name
FROM cities
WHERE name = (
    SELECT name
    FROM states
    WHERE name = 'California')
ORDER BY id;
