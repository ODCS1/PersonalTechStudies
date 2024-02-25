-- SUBQUERY (SUBSELECT)

-- MONTE UM RELATÓRIO QUE TENHA TODOSOS PRODUTOS CADASTRADOS E TENHAM UM PREÇO DE VENDA ACIMA DA MÉDIA.

SELECT *
FROM Production.Product
WHERE ListPrice > (SELECT AVG(ListPrice) FROM Production.Product)


-- Eu quero saber saber o nome dos meus funcionários que tem o cargo de 'Design Engineer'

SELECT FirstName
FROM Person.Person
WHERE (SELECT JobTitle FROM HumanResources.Employee) = 'Design Engineer'

-- FAZENDO COM JOIN
SELECT A.FirstName
FROM Person.Person A
INNER JOIN HumanResources.Employee B ON A.BusinessEntityID = B.BusinessEntityID AND B.JobTitle = 'Design Engineer'