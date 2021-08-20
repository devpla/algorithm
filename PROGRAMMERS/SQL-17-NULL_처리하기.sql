SELECT
  animal_type            AS animal_ins_type,
  NVL(name, 'No name')   AS animal_ins_name,
  sex_upon_intake        AS animal_ins_sex_upon_intake
FROM animal_ins
ORDER BY animal_id
