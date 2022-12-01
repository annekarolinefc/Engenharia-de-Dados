--TRIM— remove espaços
--REPLACE— substitui algo por algo
--LPAD e REPLICATE— Replica valores
--SUBSTRING— pega trecho de um texto
--UPPER— deixa tudo maiúsculo
--LOWER— deixa tudo minúsculo
--LEN— calcula a quantidade de caracteres

SELECT p.codigoProduto, -- Informação original
       p.NomeProduto, -- Informação original                 
       TRIM(p.NomeProduto)               AS TRIM, -- removendo espaços da coluna NomeProduto (o AS é dando um Alias, ou seja, um apelido para a coluna)
       REPLACE(p.NomeProduto, 'A', 'AA') AS "REPLACE", -- Substituido onde tiver A por AA no Tipo de Produto
       LPAD(p.CodigoProduto, 9, "0")     AS LPAD,  -- Adiciona zeros a esquerda no código do produto até completar 9 dígitos
       SUBSTRING(p.NomeProduto, 1, 3)    AS SUBSTRING, -- Pega os primeiros 3 caracteres da coluna de Nome do Produto 
       UPPER(p.NomeProduto)              AS UPPER, -- Nome de Produto em maiúsculo
       LOWER(p.NomeProduto)              AS LOWER, -- Nome de Produto em minúsculo
       LENGTH(p.NomeProduto)             AS LENGTH -- Quantos caracteres tem o campo NomeProduto
  FROM dim_produto AS p -- o AS aqui, também é Alias, um apelido aqui no caso para Tabelas;