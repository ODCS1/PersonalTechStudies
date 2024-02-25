-- MANIPULAÇÃO DE STRING

-- CONCATENAR
SELECT CONCAT(FirstName, ' ', LastName)
FROM Person.Person

-- MAIÚSCULO
SELECT UPPER(FirstName)
FROM Person.Person

-- MINÚSCULO
SELECT LOWER(FirstName)
FROM Person.Person

-- LEN
SELECT FirstName, LEN(FirstName)
FROM Person.Person

-- SUBSTRING
SELECT FirstName, SUBSTRING(FirstName, 1, 3)
FROM Person.Person

-- REPLACE
SELECT ProductNumber, REPLACE(ProductNumber, '-', '#')
FROM Production.Product

-- DESAFIO

SELECT CONCAT(UPPER(FirstName), ' ', MiddleName, ' ', LOWER(LastName)) AS 'NOME COMPLETO', LEN(FirstName) AS 'Tamanho Nome'
FROM Person.Person


SELECT REPLACE(Name, ' ', '-') AS Nome, SUBSTRING(ProductNumber, 4, 7) AS 'Número Produto'
FROM Production.Product