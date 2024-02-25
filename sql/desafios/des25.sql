SELECT TOP 10 *
FROM Person.StateProvince

SELECT TOP 10 *
FROM Person.Address

-- AdressId, City, StateProvinceId, Node do Estado


-- RESPOSTA
SELECT PA.AddressID, PA.City, PA.StateProvinceID, PSP.Name
FROM Person.Address PA
INNER JOIN Person.StateProvince PSP ON PA.StateProvinceID = PSP.StateProvinceID