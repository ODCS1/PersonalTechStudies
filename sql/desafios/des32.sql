-- CRIE 2 TABELAS NOVAS E INSIRA A RESTRIÇÃO  NOT NULL

CREATE TABLE NovaTabela (
    id int PRIMARY KEY,
    codigo int NOT NULL,
    acesso VARCHAR(20) NOT NULL
);

CREATE TABLE OutraTabela (
    id int PRIMARY KEY,
    valido VARCHAR(10) NOT NULL,
    valor_conta DECIMAL(10,2) NOT NULL
);
