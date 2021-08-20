SELECT name
FROM (

    SELECT name
    FROM animal_ins
    ORDER BY datetime

)
WHERE ROWNUM = 1
