-- -------------
-- Left Join --
-- -------------

-- O Left Join tem como resultado todos os registros que estão na tabela A (mesmo que não estejam na tabela B) 
-- e os registros da tabela B que são comuns à tabela A.
SELECT *
  FROM      fato_vendas ven
  LEFT JOIN dim_produto pro ON pro.CodigoProduto = ven.CodigoProduto;
