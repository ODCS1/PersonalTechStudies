-- Obter o nome e numero do produto dos produtos que tem o ProductID entre 1-4.

SELECT TOP 4 productnumber, name
FROM production.product
ORDER BY productid asc