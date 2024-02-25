-- Eu quero saber qual foram as 10 vendas que no total tiveram os maiores valores de venda(line total) por produto do maior valor para o menor.


SELECT TOP 10(SalesOrderDetailID), SUM(LineTotal) AS 'VALOR'
FROM Sales.SalesOrderDetail
GROUP BY SalesOrderDetailID
ORDER BY SUM(LineTotal) DESC