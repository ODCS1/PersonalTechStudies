-- Um usuário Peter Krebs está devendo um pagamento, consiga o email dele para que possamos enviar uma cobrança!

SELECT BusinessEntityID,firstname,lastname
FROM person.person
WHERE firstname = 'Peter' and lastname = 'Krebs'

-- 26

SELECT BusinessEntityID,emailaddress
FROM person.EmailAddress
WHERE BusinessEntityID = 26