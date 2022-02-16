SELECT DISTINCT(p.name)
FROM stars s
join people p
  on p.id = s.person_id
join movies m
  on m.id = s.movie_id
WHERE m.year = 2004
ORDER BY p.birth;