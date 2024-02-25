-- Sendo que se trata de uma multinacional os gerentes querem saber quais produtos (productid) não estão trazendo em média no mínimo 1 milhão em total de vendas (lineTotal)

SELECT ProductID, AVG(LineTotal) AS 'Valor médio'
FROM Sales.SalesOrderDetail
GROUP BY ProductID
HAVING AVG(LineTotal) < 1000000