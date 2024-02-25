-- CRIAR UMA TABELA NOVA COM 3 COLUNAS E DEPOIS:

1 - Alterar o tipo da coluna
2 - Renomear o nome de uma coluna
3 - Renomear o nome da tabela que você criou


CREATE TABLE Escola (
    id_escola int PRIMARY KEY,
    nome_escola varchar(50) NOT NULL,
    qtd_alunos int,
    qtd_funcionarios int
)

ALTER TABLE Escola
ALTER COLUMN qtd_funcionarios tinyint

EXEC sp_RENAME 'nome_escola', 'nome', 'COLUMN'

EXEC sp_RENAME 'Escola', 'Escola2'