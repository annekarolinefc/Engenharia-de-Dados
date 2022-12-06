-- BETWEEN — Entre valores

SELECT distinct 
       CodigoCliente, 
       CodigoProduto 
  FROM fato_vendas
 WHERE CodigoProduto IN (1, 2)
   AND CodigoCliente BETWEEN 1 AND 3