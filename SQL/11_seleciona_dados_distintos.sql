-- Seleciona os registros distintamente (não aparecerão linhas repetidas)

SELECT DISTINCT CodigoCliente, CodigoProduto 
FROM Vendas 
WHERE CodigoCliente = 5