-- DECLARAÇÃO DE VARIÁVEIS

-- SINTAXE
DECLARE @var1 INT,
        @var2 INT = 2,
        @var3 NVARCHAR(100) = 'Maria Joana';


-- EXEMPLO
DECLARE @nome NVARCHAR(100) = FirstName,
        @sobrenome  NVARCHAR(60) = LastName,
        @identifica INT = BusinessEntityID;


-- EXEMPLO 2
BEGIN
	DECLARE	@QuantosRegistros INT = 1,
			@categoria INT,
			@acesso NVARCHAR(100) = 'O';
	SET @categoria = 18;
	SET	@acesso = + N' ADMINISTRADOR';

	DECLARE @identificacao INT,
			@Titulo NCHAR(3),
			@Nome NVARCHAR(100),
			@Sobrenome NVARCHAR(100);
	SELECT
		@identificacao = BusinessEntityID, 
		@Titulo = Title, 
		@Nome = FirstName, 
		@Sobrenome = LastName
	FROM
		Person.Person
	WHERE
		BusinessEntityID = 6;

	print 'Business Entity ID: ' + CAST(@identificacao AS VARCHAR)
	print 'Título: ' + CAST(@Titulo AS VARCHAR)
	print 'Olá, ' + @Nome + ' ' + @Sobrenome + '!'
END