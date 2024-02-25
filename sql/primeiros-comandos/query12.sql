-- HAVING

-- O HAVING é basicamente muito usado em junção com o GROUP BY para filtrar resultados de um agrupamento.

-- De uma forma mais simples é basicamente um where para dados agrupados.

SELECT coluna1, funcaoAgregacao(coluna)
FROM nomeTabela
GROUP BY coluna1
HAVING condicao;

-- DIFERENÇA ENTRE O WHERE E O HAVING

-- O GROUP BY é plicado depois dos dados serem agrupados, enquanto o WHERE é aplicado antes dos dados serem agrupados.

-- EXEMPLO 1
SELECT FirstName, COUNT(FirstName) as 'Quantidade'
FROM Person.Person
GROUP BY FirstName
HAVING COUNT(FirstName) > 10;


-- EXEMPLO 2
SELECT ProductID, SUM(LineTotal) as 'Valor Total'
FROM Sales.SalesOrderDetail
GROUP BY ProductID
HAVING SUM(LineTotal) between 162000 AND 500000


-- EXEMPLO 3
SELECT FirstName, COUNT(FirstName) as 'Quantidade'
FROM Person.Person
WHERE Title = 'Mr.'
GROUP BY FirstName
HAVING COUNT(FirstName) > 10