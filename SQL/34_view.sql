-- VIEW — Em SQL, uma view é uma tabela virtual baseada no conjunto de resultados de uma instrução SQL.


CREATE OR REPLACE VIEW vwvendas_resumida as
SELECT ven.DataVenda   AS Data
     , cli.NomeCliente AS Cliente
     , pro.NomeProduto AS Produto
  FROM fato_vendas ven
  JOIN dim_cliente cli on cli.CodigoCliente = ven.CodigoCliente
  JOIN dim_produto pro on pro.CodigoProduto = ven.CodigoProduto;

-- Consultando a View (basta passarmos essa View ao usuário)
SELECT * FROM vwvendas_resumida;