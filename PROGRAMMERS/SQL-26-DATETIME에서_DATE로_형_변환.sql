SELECT
  animal_id                       AS ins_animal_id,
  name                            AS ins_animal_name,
  TO_CHAR(datetime, 'yyyy-mm-dd') AS ins_animal_date
FROM animal_ins
ORDER BY animal_id
