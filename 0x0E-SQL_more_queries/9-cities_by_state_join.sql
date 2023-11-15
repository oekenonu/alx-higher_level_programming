-- lists cities in database hbtn_0d_usa
SELECT C.id, C.name, S.name 
FROM cities as C
INNER JOIN states as S
ON S.id = C.state_id 
ORDER BY C.id;
