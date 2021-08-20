SELECT
  animal_id,
  animal_name
FROM (

    SELECT
      ins.animal_id                   AS animal_id,
      ins.name                        AS animal_name,
      (outs.datetime - ins.datetime)  AS term
    FROM animal_ins ins
    JOIN animal_outs outs
      ON ins.animal_id = outs.animal_id
    ORDER BY term DESC

)
WHERE ROWNUM <= 2
