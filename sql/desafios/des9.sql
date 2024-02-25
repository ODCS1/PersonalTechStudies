-- Obter o Productid dos 10 produtos mais caros cadastrados no sistema, listando do mais caro par o mais barato.

SELECT TOP 10 productid,listprice
FROM production.product
ORDER BY listprice desc