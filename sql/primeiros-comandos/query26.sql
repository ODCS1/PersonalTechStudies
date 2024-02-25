-- INSERT INTO

-- Preencher dados nas colunas de um tabela

INSERT INTO nomeTabela(coluna1, coluna2...)
VALUES (valor1, valor2...)
VALUES (valor1, valor2...)
VALUES (valor1, valor2...)



Colocando valores em uma tabela com dados já existentes em outra tabela.

INSERT INTO TabelaA (coluna1)
SELECT coluna2
FROM TabelaB


-- EXEMPLO 1
CREATE TABLE aula (
  id int PRIMARY KEY,
  nome VARCHAR(200)
)

INSERT INTO aula(id,nome)
VALUES
  (1, 'aula 1'),
  (2, 'aula 2'),
  (3, 'aula 3');


-- EXEMPLO 2

SELECT * INTO tbl_nova FROM aula