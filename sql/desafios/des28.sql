-- Encontre para mim todos os endereços que estão no estado de 'Alberta', pode trazer todas informações

SELECT * FROM 
Person.Address
WHERE StateProvinceID IN (SELECT StateProvinceID FROM Person.StateProvince WHERE Name = 'Alberta')