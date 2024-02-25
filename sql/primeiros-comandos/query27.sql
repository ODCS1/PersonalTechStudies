-- UPDATE

O UPDATE será utilizado para alterar linhas no banco de dados.

UPDATE nomeTabela
SET coluna1 = valor1
    coluna2 = valor2
WHERE condicao


-- EXEMPLO

UPDATE aula
SET nome = 'teste'
WHERE id = 3


-- DESAFIO

UPDATE tbl_nova
SET nome = 'Novo Nome'
WHERE id < 3