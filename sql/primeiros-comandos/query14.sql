-- INNER JOIN

-- EXISTE 3 TIPOS DE JOIN

-- INNER JOIN, OUTER JOIN E SELF-JOIN

-- O INNER JOIN SERVE PARA JUNTAR CONLUNAS DE TABELAS DIFERENTES.

SELECT C.ClienteId, C.Nome, E.Rua, E.Cidade
FROM Cliente C
INNER JOIN Endereco E ON C.EnderecoId = E.EnderecoId

-- EXEMPLO 1

SELECT P.BusinessEntityID, P.FirstName, P.LastName, E.EmailAddress
FROM Person.Person P
INNER JOIN Person.EmailAddress E ON P.BusinessEntityID = E.BusinessEntityID


-- EXEMPLO 2

SELECT P.Name, P.ListPrice, PS.Name AS 'SUBCATEGORIA'
FROM Production.Product P
INNER JOIN Production.ProductSubcategory PS ON P.ProductSubcategoryID = PS.ProductSubcategoryID


-- EXEMPLO 3

SELECT TOP 10 *
FROM PersonBusinessEntityAdress BA
INNER JOIN Person.Adress PA ON BA.AdressID = PA.AdressID