-- Eu preciso saber em média qual é a quantidade(quantity) que cada produto é vendido na loja.

SELECT ProductID, AVG(OrderQty) AS 'Qtd média'
FROM Sales.SalesOrderDetail
GROUP BY ProductID