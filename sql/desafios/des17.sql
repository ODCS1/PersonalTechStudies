/*
    Eu preciso saber quantas pessoas tem o mesmo MiddleName agrupadas por o MiddleName
*/


SELECT MiddleName, COUNT(MiddleName) AS 'CONTAGEM'
FROM Person.Person
GROUP BY MiddleName