-- -------------
-- Right Join --
-- -------------

-- Usando o Right Join teremos como resultado todos os registros que estão na tabela B (mesmo que não estejam na tabela A) 
-- e os registros da tabela A que são comuns à tabela B.

SELECT * FROM fato_vendas;
SELECT * FROM dim_produto;

SELECT *
  FROM       fato_vendas ven
  RIGHT JOIN dim_produto pro ON pro.CodigoProduto = ven.CodigoProduto;