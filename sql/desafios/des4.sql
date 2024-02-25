-- Foi pedido pelo marketing uma relação de todos os empregados(employees) que são casados (single=solteiro, married=casado) e são asalariados (salaried)

SELECT *
FROM HumanResources.Employee
WHERE MaritalStatus = 'm' and SalariedFlag = 1