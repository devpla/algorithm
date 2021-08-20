SELECT
  animal_id     AS ins_animal_id,
  name          AS ins_animal_name,
  CASE
    WHEN sex_upon_intake LIKE 'Intact%'
      THEN 'X'
    ELSE 'O'
  END           AS has_been_spayed
FROM animal_ins
ORDER BY animal_id
