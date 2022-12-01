-- O UNION operador é usado para combinar o conjunto de resultados de dois ou mais SELECT.

-- Cada SELECT dentro UNIONdeve ter o mesmo número de colunas
-- As colunas também devem ter tipos de dados semelhantes
-- As colunas em cada SELECT também devem estar na mesma ordem

SELECT CodigoCliente, CodigoProduto 
  FROM FATO_VENDAS
 WHERE CodigoProduto = 2
UNION
SELECT CodigoCliente, CodigoProduto 
  FROM FATO_VENDAS
 WHERE CodigoProduto = 3;