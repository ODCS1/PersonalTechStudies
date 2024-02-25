-- Quantos produtos vermelhos tem preço entre 50 a 1000 dólares.

SELECT COUNT(listprice)
FROM production.product
WHERE listprice BETWEEN 500 AND 1000 AND color = 'red'

-- 11