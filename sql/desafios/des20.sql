-- Eu preciso saber quantos produtos e qual a quantidade média de produtos temos cadastrados nas nossas ordem de serviços (WorkOrder), agrupadas por productid.

SELECT productID, COUNT(StockedQty) AS 'Contagem', AVG(StockedQty) AS 'Média produtos'
FROM Production.WorkOrder
GROUP BY ProductID