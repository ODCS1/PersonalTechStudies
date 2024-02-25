-- Between - Usado para encontrar um valor mínimo e um valor máximo.

valor BETWEEN mínimo AND máximo;

-- É a mesma coisa que dizer:
valor >= mínimo AND valor <= máximo;

-- Ex:

SELECT *
FROM production.product
WHERE listprice BETWEEN 1000 AND 1500;