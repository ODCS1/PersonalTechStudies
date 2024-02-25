SELECT TOP 10 *
FROM Person.PhoneNumberType


SELECT TOP 10 *
FROM Person.PersonPhone

-- BusinessEntityId, Name, PhoneNumberTypeId, PhoneNumber

-- RESPOSTA
SELECT P.BusinessEntityID, PT.Name, P.PhoneNumberTypeId, P.PhoneNumber
FROM Person.PhoneNumberType PT
INNER JOIN Person.PersonPhone P ON PT.PhoneNumberTypeId = P.PhoneNumberTypeId