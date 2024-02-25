-- NOT NULL CONSTRAINT

CREATE TABLE CarteiraMotorista (
    Id int NOT NULL,
    Nome VARCHAR(255) NOT NULL,
    Idade int CHECK (Idade >= 18)
)

INSERT INTO CarteiraMotorista (Id, Nome, Idade)
VALUES
    (1, 'Jhonatan', 19)