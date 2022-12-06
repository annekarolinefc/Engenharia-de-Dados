--    Seleciona distintamente as colunas: CodigoCliente e CodigoProduto da tabela: fato_vendas, apenas os registros onde o NomeProduto SEJA Nulo.

SELECT distinct 
       v.CodigoCliente, 
       v.CodigoProduto,
       p.NomeProduto
  FROM fato_vendas v
 RIGHT JOIN dim_produto p on p.CodigoProduto = v.CodigoProduto
 WHERE p.NomeProduto IS NULL; -- IS NOT NULL