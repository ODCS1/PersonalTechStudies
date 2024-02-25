-- LIKE
-- Vamos dizer que você queira encontrar uma pessoa no banco de dados que vc sabe que o nome dela era ovi...alguma coisa

SELECT *
FROM person.person
WHERE firstname like 'ovi%'

-- Outro exemplo:

SELECT *
FROM person.person
WHERE firstname LIKE '%to'

-- Outro exemplo:

SELECT *
FROM person.person
WHERE firstname LIKE '%essa%'

-- Outro exemplo:
-- O Underline vai substituir apenas 1 caracter após o 'ro':
SELECT *
FROM person.person
WHERE firstname LIKE '%ro_'
