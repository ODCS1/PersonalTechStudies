-- CHECK

CHECK TAMBÉM PODE SER CHAMADA DE RESTRIÇÃO DE VERIFICAÇÃO.

É UMA CLÁUSULA USADA NA DEFINIÇÃO DE CAMPOS DE TABELAS QUE PERMITE ESTABELECER CONDIÇÕES DE VERIFICAÇÃO DA CONSISTÊNCIA DE VALORES INSERIDOS OU ALTERADOS NESSES CAMPOS.

ELA É USADA PARA ESPECIFICAR QUAIS VALORES SÃO ACEITÁVEIS EM UM OU MAIS CAMPOS. 

COMO SE TRATA DE UMA CONDIÇÃO, USAMOS EXPRESSÕES LÓGICAS QUE RETORNEM true OU false PARA ESPECIFICAR O CRITÉRIO DE VALIDAÇÃO DO CAMPO.

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
(3, "Nome3", 31)


-- EXEMPLO
create table Estoque.Venda
(
idVenda int identity primary key,
idProduto int not null,
dataInclusaoNoEstoque date not null,
quantidadeVendida float not null check (quantidadeVendida >= 0),
CPFComprador char(14)
CHECK (CPFComprador like '[0-9][0-9][0-9].[0-9][0-9][0-9].[0-9][0-9][0-9]-[0-9][0-9]'),
CEPComprador char(8) CHECK (CEPComprador like '[0-9][0-9][0-9][0-9][0-9]-[0-9][0-9]'),
dataVenda Date CHECK (dataVenda >= dataInclusaoNoEstoque),
foreign key (idProduto) references Estoque.Produto(idProduto)
)