SELECT * FROM Empresa.TRABALHA_EM;

SELECT * FROM Empresa.DEPTO_LOCAIS;

SELECT * FROM Empresa.V_Onde_Trabalha;

CREATE TRIGGER Empresa.TGR_idade_empregado
	ON Empresa.Empregado
	FOR INSERT, UPDATE AS
BEGIN
	DECLARE @idade int, @numSeg char(9), @anoAtual char(10), @anoNasc char(10)
	SELECT @numSeg = numSegSocial, @anoNasc = dataNascimento
	FROM inserted
END
GO