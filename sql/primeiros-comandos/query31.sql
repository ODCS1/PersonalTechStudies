-- CHECK CONSTRAINT

-- Criar restrições no momento de criação das tabelas


-- EXEMPLO
CREATE TABLE CarteiraMotorista (
    id int NOT NULL,
    Nome varchar(255) NOT NULL,
    Idade int CHECK (Idade >= 18)
);

INSERT INTO CarteiraMotorista (id, Nome, Idade)
VALUES
(1, "Nome1", 19),
(2, "Nome2", 20),
(3, "Nome3", 133),
(4, "Nome4", 16)

The INSERT statement conflicted with the CHECK constraint "CK__CarteiraM__Idade__412EB0B6". The conflict occurred in database "YouTube", table "dbo.CarteiraMotorista", column 'Idade'.