SELECT
  name,
  datetime
FROM animal_ins
WHERE animal_id NOT IN (

    SELECT animal_id
    FROM animal_outs

)
ORDER BY datetime
FETCH NEXT 3 ROWS ONLY;
