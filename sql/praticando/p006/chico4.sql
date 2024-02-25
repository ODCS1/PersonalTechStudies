-- a
SELECT prenome
FROM 
    departamento.empregado
WHERE
    depto = 5 AND
    horas_trab > 20 AND
    project = 'ProdutoX'

-- b

SELECT prenome
FROM 
    departamento.empregado
WHERE
    nome_dependente = prenome