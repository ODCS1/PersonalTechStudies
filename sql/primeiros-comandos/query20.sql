-- DATEPART

DATEPART( datepart, date )

SELECT SalesOrderID, DATEPART(MONTH, OrderDate) AS 'MÊS'
FROM Sales.SalesOrderHeader



SELECT AVG(TotalDue) AS 'Média', DATEPART(MONTH, OrderDate) AS 'MÊS'
FROM Sales.SalesOrderHeader
GROUP BY  DATEPART(MONTH, OrderDate)
ORDER BY 'MÊS'


-- DESAFIO DE PUXAR A DATA E O MÊS DE ALGUMA TABELA

SELECT DATEPART(YEAR, HireDate) AS 'Ano de entrada', DATEPART(MONTH, BirthDate) AS 'Mês aniversário'
FROM HumanResources.Employee
ORDER BY 'Ano de entrada'