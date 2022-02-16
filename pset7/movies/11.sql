SELECT title
FROM movies m
JOIN ratings r
  ON m.id = r.movie_id
JOIN stars s
  ON s.movie_id = m.id
WHERE s.person_id = (SELECT id
                  FROM people
                  WHERE name = "Chadwick Boseman")
ORDER BY r.rating DESC
LIMIT 5;