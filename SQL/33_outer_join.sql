-- -------------
-- Outer Join --
-- -------------

-- O Outer Join (também conhecido por Full Outer Join ou Full Join) tem como resultado todos os registros que estão na tabela A e todos os registros da tabela B.
-- No MySQL não tem nativamente

SELECT *
  FROM            fato_vendas ven
  LEFT OUTER JOIN dim_produto pro ON pro.CodigoProduto = ven.CodigoProduto
UNION
SELECT *
  FROM            fato_vendas ven
 RIGHT OUTER JOIN dim_produto pro ON pro.CodigoProduto = ven.CodigoProduto;