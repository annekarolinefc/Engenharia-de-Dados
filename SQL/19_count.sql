-- ------------------------------------------------------------
-- Contagem de produtos (quantos produtos temos na nossa base?)
-- ------------------------------------------------------------
SELECT count(codigoProduto) as qtd_produtos
  FROM dim_Produto;