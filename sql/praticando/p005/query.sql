SELECT prenome, endereco, E.NumDepto
FROM Empresa.empregado as E, Empresa.departamento as D
WHERE NomeDepto ='Pesquisa'AND D.NumDepto = E.NumDepto