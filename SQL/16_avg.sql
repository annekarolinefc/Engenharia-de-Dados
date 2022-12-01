-- ----------------------------------------
-- Média da quantidade de produtos vendidos
-- ----------------------------------------
SELECT AVG(quantidade)          AS media_quantidade_venda,
       round(AVG(quantidade),2) AS media_quantidade_venda_arredondado
  FROM fato_vendas;