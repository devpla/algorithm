SELECT
  animal_id,
  animal_type,
  name
FROM animal_outs
WHERE animal_id IN (

    SELECT animal_id
    FROM animal_ins
    WHERE sex_upon_intake LIKE 'I%'

)
  AND sex_upon_outcome NOT LIKE 'I%'
ORDER BY animal_id
