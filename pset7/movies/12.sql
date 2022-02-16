SELECT title
FROM movies m, stars s, people p
WHERE s.movie_id = m.id
AND p.id = s.person_id
AND name IN ("Johnny Depp", "Helena Bonham Carter")
GROUP BY title
HAVING(COUNT(title)) > 1;