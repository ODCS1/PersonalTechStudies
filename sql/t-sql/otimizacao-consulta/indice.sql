-- INDEX

-- UM INDEX SERVE PARA FAZER SELEÇÕES MAIS RÁPIDAS, A IDEIA É PARECIDA COM A BUSCA BINÁRIA

-- OBSERVE QUE OS CLÁUSULAS DE INSERT, UPDATE, DELETE E MERGE FICAM MAIS LENTAS.

-- PARA QUE O INDEX TENHA EFETIVIDADE REALMENTE, É NECESSÁRIO NAS SELEÇÕES USAR A CLÁUSULO WHERE COM AS CHAVES DESELEÇÃO ESTIPULADAS NA CRIAÇÃO DO INDEX.

CREATE [ UNIQUE ] [ CLUSTERED | NONCLUSTERED ] INDEX index_name
ON( column [ ASC | DESC ] [ ,...n ] )
[ INCLUDE ( column_name [ ,...n ] ) ]
[ WITH ( [ ,...n ] ) ]

[ ON { partition_scheme_name ( column_name )
| filegroup_name
| default
}
]
[ ; ]

-- EXEMPLO 1
Create index ixEmpregadoDepto
on Empresa.Empregado (numDepto)


-- EXEMPLO 2
CREATE INDEX ixFuncinários
ON HumanResources.Employee (BusinessEntityID)

-- EXEMPLO DE SELEÇÃO QUE UTILIZARÁ O INDEX CRIADO
SELECT * FROM HumanResources.Employee WHERE BusinessEntityID > 10

-- PARA EXCLUIR UM INDEX
drop index ixEmpregadoDepto on Empresa.Empregado