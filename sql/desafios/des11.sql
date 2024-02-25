-- Quantos produtos temos cadastrados no sistema que custam mais que 1500 dólares?

SELECT count(ListPrice)
FROM Production.Product
WHERE ListPrice > 1500

-- 39