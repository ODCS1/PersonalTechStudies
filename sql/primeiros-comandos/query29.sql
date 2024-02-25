-- ALTER TABLE

-- Alterar a estrutura de uma tabela

ALTER TABLE nomeDaTabela
ACAO

-- EXEMPLOS DO QUE PODE SER FEITO

- add, Remover, or alterar uma coluna
- Setar valores padrôes para uma coluna
- add ou Remover restrições de colunas
- Renomear uma tabela

-- EXEMPLO

CREATE TABLE youtube (
    id int PRIMARY KEY,
    nome VARCHAR(150) NOT NULL UNIQUE,
    categoria VARCHAR(200) NOT NULL,
    dataCriacao DATETIME NOTNULL
)

ALTER TABLE youtube
ALTER COLUMN categoria VARCHAR(300)

-- Para alterar o nome de uma coluna será necessário utilizar o procedure seguinte

EXEC sp_RENAME 'nomeTabela.nomeColunaAtual', 'nomeColunaNova', 'COLUMN'


-- EXEMPLO
EXEC sp_RENAME 'youtube.nome', 'nomeCanal', 'COLUMN'

-- Então para alterar o nome de uma tabela também será utilizado um procedure

EXEC sp_RENAME 'nomeTabelaAtual', 'nomeTabelaNova'

-- Exemplo

EXEC sp_RENAME 'youtube', 'tabelaMudeiNome'