-- Quantos tamanhos de produtos tem cadastrado na tabela

SELECT COUNT(*)
FROM production.product
WHERE size <> 'null'

-- 211