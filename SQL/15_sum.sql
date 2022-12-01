-- --------------------------------------------
-- Somatório da quantidade de produtos vendidos
-- --------------------------------------------
SELECT SUM(quantidade) AS quantidade_venda
  FROM fato_vendas;