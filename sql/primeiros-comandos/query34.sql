-- VIEWS

-- VIEWS SÃO TABELAS CRIADAS PARA CONSULTAS ONDE VOCÊ USA OUTRAS COMO BASE PARA CRIAR UMA NOVA TABELA DE PESQUISA COM APENAS DADOS ESPECÍFICOS QUE VOCÊ PRECISA DE UMA TABELA.


CREATE VIEW [Pessoas Simplificadas] AS 
SELECT FirstName, MiddleName, LastName
FROM Person.Person
WHERE Title = 'Ms.'

SELECT * FROM [Pessoas Simplificadas]