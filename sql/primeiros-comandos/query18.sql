-- SELF JOIN

-- É NECESSÁRIO DAR UM APELIDO PARA A TABELA.

-- SELECT NOME_COLUNA
-- FROM TABELA A, TABELA B
-- WHERE CONDICAO

-- Eu quero todos os clientes que moram na mesma região

SELECT A.ContactName, B.ContactName
FROM CUSTOMERS A, CUSTOMERS B
WHERE A.REGION = B.REGION



-- Eu quero encontrar(nome e data de contratação) detodos os funcionários que foram contratados no mesmo ano


SELECT A.EmployeeID, A.FirstName, A.HireDate, B.EmployeeID, B.FirstName, B.HireDate
FROM Employees A, Employees B
WHERE DATEPART(YEAR, A.HireDate) = DATEPART(YEAR, B.HireDate)