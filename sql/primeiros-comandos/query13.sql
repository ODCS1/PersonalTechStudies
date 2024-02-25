-- AS

-- O AS como visto anteriormento, atribuí nomes as colunas, sendo uma coluna que já possua seu respectivo nome, ou uma que não possua.

-- Detalhe que para palavras compostas, é necessário estar dentro de aspas.

-- EXEMPLO 1
SELECT TOP 10 ListPrice as Preço
FROM Production.Product


-- EXEMPLO 2
SELECT TOP 10 AVG(ListPrice) AS "Preço Médio"
FROM Production.Product