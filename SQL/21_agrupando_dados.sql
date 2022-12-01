
SELECT Estado
     , count(*)
  FROM cliente
 GROUP BY Estado;