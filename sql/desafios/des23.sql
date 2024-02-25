-- TRADUZINDO O NOME DAS COLUNAS SELECIONADAS, FAÇA OS DESAFIOS ABAIXO.

-- Encontrar o FirstName e LastName person.person

SELECT FirstName AS 'Nome', LastName AS 'Sobrenome'
FROM Person.Person

-- Encontrar o ProductNumber em Production.Product "Número do Produto"
SELECT ProductNumber  AS 'Número do Produto'
FROM Production.Product


-- Sales.SalesOrderDetail unitPrice "Preço Unitário"

SELECT unitPrice AS 'Preço Unitário'
FROM Sales.SalesOrderDetail