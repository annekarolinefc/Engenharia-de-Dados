-- São funções embutidas (built-in) aplicadas sobre uma coleção de valores (colunas) de um banco de dados - NÃO PODEM SER UTILIZADAS NA CLÁUSULA WHERE

-- SUM— Retorna o somatório dos valores de uma coleção
-- AVG — Retorna a média dos valores de uma coleção
-- MAX— Retorna o maior valor de uma coleção de valores
-- MIN — Retorna o menor valor de uma coleção
-- COUNT — Retorna o número de elementos de uma coleção

-- ROUND— Arredondamento de valores


-- ------------------------------------------------------------
-- Visualização unica
-- ------------------------------------------------------------
SELECT SUM(quantidade) AS qtd, 'Quantidade de Venda - Somatório' as descricao FROM fato_vendas
union
SELECT round(AVG(quantidade),2) AS qtd, 'Quantidade de Venda - Média' as descricao FROM fato_vendas
union
SELECT MAX(quantidade) AS qtd, 'Quantidade de Venda - Máxima' as descricao FROM fato_vendas
union
SELECT MIN(quantidade) AS qtd, 'Quantidade de Venda - Minima' as descricao FROM fato_vendas
union
SELECT count(codigoProduto) AS qtd, 'Quantidade de Produtos - Count' as descricao FROM dim_Produto;

/* Lendo o comando: 
   Usamos o Comando ROUND para arredondar valores (para duas casas decimais)
   Aqui vou começar a utilizar outras tabelas e mais campos. Além de mais alguns recursos, como Alias (apelidos)
   Lembre-se sempre, se puder ser o mais especifíco em relação as colunas que vai utilizar, melhor.
*/