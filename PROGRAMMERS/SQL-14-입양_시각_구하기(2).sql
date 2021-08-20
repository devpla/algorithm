SELECT
  hour_filter                             AS animal_outs_hour,
  NVL(outs_count, 0)                      AS animal_outs_count
FROM (

    SELECT
      TO_NUMBER(TO_CHAR(datetime, 'HH24')) AS outs_hour,
      COUNT(*)                             AS outs_count
    FROM animal_outs
    GROUP BY TO_NUMBER(TO_CHAR(datetime, 'HH24'))

  )
RIGHT OUTER JOIN(

    SELECT ROWNUM-1                        AS hour_filter
    FROM animal_outs
    WHERE ROWNUM <= 24
)
ON outs_hour = hour_filter
ORDER BY animal_outs_hour
