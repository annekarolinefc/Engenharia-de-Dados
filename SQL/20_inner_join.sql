-- -------------
-- Inner Join --
-- -------------


-- O Inner Join é o método de junção mais conhecido e retorna os registros que são comuns às duas tabelas.
SELECT * FROM fato_vendas;
SELECT * FROM dim_produto;

-- Relacionando a tabela de vendas com a de produtos
SELECT *
  FROM       fato_vendas ven
  INNER JOIN dim_produto pro ON pro.CodigoProduto = ven.CodigoProduto;