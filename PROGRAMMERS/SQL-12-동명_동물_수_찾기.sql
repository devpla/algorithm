SELECT
  name        AS animal_name,
  COUNT(name) AS animal_count
FROM animal_ins
GROUP BY name
HAVING COUNT(name) >= 2
ORDER BY name ASC
