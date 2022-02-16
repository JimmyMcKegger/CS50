SELECT DISTINCT(p.name)
FROM people p, movies m, stars s
WHERE p.id = s.person_id
AND s.movie_id = m.id
AND s.movie_id IN (
  SELECT movie_id FROM stars WHERE person_id = (
    SELECT id
    FROM people
    WHERE name = 'Kevin Bacon'
    AND birth = 1958
  )
)
AND NOT p.name = 'Kevin Bacon';