-- Quantos produtos cadastrados tem a palavra 'road' no nome deles.

SELECT COUNT(*)
FROM Production.Product
WHERE name LIKE '%road%'

-- 103