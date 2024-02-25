-- UNIQUE CONSTRAINT


CREATE TABLE CarteiraMotorista (
    Id int NOT NULL,
    Nome VARCHAR(255) NOT NULL,
    Idade int CHECK(idade > 17),
    CodigoCNH int NOT NULL UNIQUE
);