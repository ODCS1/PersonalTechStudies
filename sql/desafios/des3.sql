-- A equipe de produção de produtos precisa do nome de todas as peças que pesam mais que 500kg mas não mais que 700kg para inspeção.

SELECT name,weight
FROM production.product
WHERE weight > 500 and weight <= 700