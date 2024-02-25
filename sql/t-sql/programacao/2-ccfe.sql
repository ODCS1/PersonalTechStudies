-- COMANDOS DE CONTROLE DE FLUXO DE EXECUÇÃO


-- IF ...ELSE
-- WHILE
-- BEGIN... END
-- Outras palavras-chave, por exemplo, são BREAK, CONTINUE, WAITFOR e RETURN, usadas para dar suporte a operações de controlede fluxo T-SQL.

-- EXEMPLO 1
IF OBJECT_ID('dbo.Canal2') IS NOT NULL
    DROP TABLE dbo.Canal2
GO

OBJECT_ID() é uma função embutida que retorna a identificação de um objeto qualquer no banco de dados.

Se não existir, retorna NULL.


-- EXEMPLO 2
IF OBJECT_ID('dbo.Pessoa') IS NULL
    BEGIN
        PRINT 'O objeto especificado, não existe!'
    END
ELSE
    BEGIN
        PRINT 'O objeto especificado, existe!'
    END


-- EXEMPLO 3
BEGIN
	DECLARE	@BusinessEntityID INT,
			@FirstName NVARCHAR(100),
			@LastName NVARCHAR(100);

	IF EXISTS (SELECT * FROM Person.Person WHERE BusinessEntityID = 8)
		BEGIN
			SELECT
				@BusinessEntityID = BusinessEntityID, @FirstName = FirstName, @LastName = LastName
			FROM
				Person.Person
			WHERE
				BusinessEntityID = 8

			PRINT @FirstName + 
			' ' + 
			@LastName + 
			' com BusinessEntityID igual a ' 
			+ CAST(@BusinessEntityID AS VARCHAR) + '!'
		END
	ELSE
		BEGIN
			PRINT 'OBJETO NÃO ENCONTRADO!'
		END
END


-- WHILE

-- EXEMPLO 4
DECLARE @BusinessEntityID INT = 1, @FirstName NVARCHAR(100);
WHILE @BusinessEntityID <= 100
	BEGIN
		SELECT @FirstName = FirstName
		FROM Person.Person
		WHERE BusinessEntityID = @BusinessEntityID
		
		PRINT CAST(@BusinessEntityID AS VARCHAR) + ' ' + @FirstName
		SET @BusinessEntityID += 1
	END