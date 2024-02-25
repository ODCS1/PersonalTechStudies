-- Quantas pessoas temos com o sobrenome que inicia com a letra P ?

SELECT COUNT(lastname)
FROM person.person
WHERE lastname LIKE 'P%'

-- 1187