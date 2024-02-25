-- Eu quero saber na tabela do pedido [Order Details] quais produtos tem o mesmo percentual de desconto


SELECT A.ProductID, B.ProductID
FROM [Order Details] A, [Order Details] B
WHERE (100 * A.Discount) / A.UnitPrice = (100 * B.Discount) / B.UnitPrice