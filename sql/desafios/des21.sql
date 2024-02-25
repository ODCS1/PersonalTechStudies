-- Estamos querendo identificar as provincias(stateProvinceId) com o maior numero de cadastros no nosso sistema, então é preciso encontrar quais provincias (stateProvinceId) estão registradas no banco de dados mais que 1000 vezes.

SELECT StateProvinceID, COUNT(StateProvinceID) AS 'Quantidade'
FROM Person.Address
GROUP BY StateProvinceID
HAVING COUNT(StateProvinceID) > 1000