-- LIKE — Contenha algo (mais voltado a texto)
SELECT distinct 
       v.CodigoCliente, 
       v.CodigoProduto,
       p.NomeProduto
  FROM fato_vendas v
  JOIN dim_produto p on p.CodigoProduto = v.CodigoProduto
 WHERE p.NomeProduto LIKE '% CH'