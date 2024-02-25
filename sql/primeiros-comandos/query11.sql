-- GROUP BY

 O GROUP BY basicamente divide o resultado da sua pesquisa em grupos.
 - Para cada grupo você pode aplicar uma função de agregação, por exemplo:
  - calcular a soma de itens
  - contar o número de itens naquele grupo


SELECT colunaq, funcaoAgregacao(coluna2)
FROM nomeTabela
GROUP BY coluna1

-- Exemplo:
SELECT specialofferid, SUM(unitprice) AS 'Soma'
FROM sales.salesorderdetail
GROUP BY specialofferid

-- Exemplo:
SELECT productid, count(productid) AS 'Contagem'
FROM sales.salesorderdetail
GROUP BY productid

-- Exemplo:
SELECT firstname, count(firstname) AS 'Contagem'
FROM person.person
GROUP BY firstname

-- Exemplo:
SELECT SalesOrderDetailID, SUM(UnitPrice) AS 'Valor total'
FROM Sales.SalesOrderDetail
GROUP BY SalesOrderDetailID