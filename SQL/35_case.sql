-- CASE — Controle de Fluxo


SELECT CodigoProduto,
       NomeProduto,
	   CASE WHEN SaldoProduto > 10 AND StatusProduto = 'Ativo' THEN 'Disponível para Venda'
       ELSE 'Estoque insuficiente' END  StatusVenda
  FROM dim_Produto