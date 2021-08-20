SELECT
  TO_CHAR(datetime, 'HH24') AS outs_hour,
  COUNT(*)                  AS outs_count
FROM animal_outs
WHERE TO_CHAR(datetime, 'HH24') BETWEEN 09 AND 19
GROUP BY TO_CHAR(datetime, 'HH24')
ORDER BY outs_hour
