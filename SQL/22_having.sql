-- A cláusula HAVING foi adicionada ao SQL porque a palavra-chave WHERE não pode ser usada com funções agregadas.

SELECT Estado
     , count(*)
  FROM cliente
 GROUP BY Estado
 HAVING count(*) > 1;