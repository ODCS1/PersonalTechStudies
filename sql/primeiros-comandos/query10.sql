-- MIN MAX SUM AVG

-- Funções de agregação basicamente agregam ou combinam dados de uma tabela em 1 resultado só.


-- SUM -> Soma todos os valores da coluna
SELECT TOP 10 SUM(linetotal) AS 'SOMA'
FROM sales.salesorderdetail

-- MIN -> Procura o menor valor da coluna
SELECT TOP 10 MIN(linetotal) AS 'Mínimo'
FROM sales.salesorderdetail

-- MAX -> Procura o maior valor da coluna
SELECT TOP 10 MAX(linetotal) AS 'Máximo'
FROM sales.salesorderdetail

-- AVG -> Mostra a média da coluna
SELECT TOP 10 AVG(linetotal) AS 'Média'
FROM sales.salesorderdetail

