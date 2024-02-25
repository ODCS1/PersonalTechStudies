-- CRIE 2 TABELAS NOVASE CRIE DUAS RESTRIÇÕES PARA ELAS

CREATE TABLE Pessoa (
    id_pessoa int PRIMARY KEY,
    nome_pessoa VARCHAR(50),
    altura DECIMAL(10,2)
    CHECK(altura > 1.60)
)


INSERT INTO Pessoa (id_pessoa, Nome_pessoa, altura)
VALUES
(1, 'Nome1', 1.72),
(2, 'Nome2', 1.95),
(3, 'Nome3', 1.33)


CREATE TABLE Carro (
    id int PRIMARY KEY,
    nome VARCHAR(50) NOT NULL,
    valor DECIMAL(10,2) NOT NULL
    CHECK(valor >= 1000000)
)

INSERT INTO Carro (id, nome, valor)
VALUES
(1, 'Carro1', 1860500),
(2, 'Carro2', 3550000),
(3, 'Carro3', 100000)