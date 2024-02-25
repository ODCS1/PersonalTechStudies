-- SQL AULA 32 DROP TABLE

-- Crie 2 tabelas e depois exclua elas

CREATE TABLE Casa (
    id_casa int PRIMARY KEY,
    nome_casa varchar(30) UNIQUE,
    qtd_led int NOT NULL
)

CREATE TABLE Comodo (
    id_comodo int PRIMARY KEY,
    nome_comodo VARCHAR(30) NOT NULL,
)

DROP TABLE Casa
DROP TABLE Comodo