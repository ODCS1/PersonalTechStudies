-- Create table 

CREATE TABLE nomeTabela (
  coluna1 tipo restricaoDaColuna,
  coluna2 tipo restricaoDaColuna,
  coluna3 tipo restricaoDaColuna,
  ....
);

-- Principais tipos de restrições

NOT NULL - Não permite nulos
UNIQUE - Força que todos os valores em uma coluna sejam diferentes
PRIMARY KEY - Uma junção de NOT NULL e UNIQUE
FOREIGN KEY - Identifica únicamente uma linha em outra nomeTabela
CHECK - Força uma condição específica em uma coluna
DEFAULT - Força um valor padrão quando nenhum valor é passado

-- Criação de exemplo

CREATE TABLE Canal (
  CanalId INT PRIMARY KEY,
  Nome VARCHAR(150) NOT NULL,
  Contageminscritos INT DEFAULT 0,
  DataCriacao DATETIME NOT NULL
);

CREATE TABLE Video (
  VideoID INT PRIMARY KEY,
  Nome VARCHAR(150) NOT NULL,
  Visualizações INT DEFAULT 0,
  Likes INT DEFAULT 0,
  Dislikes INT DEFAULT 0,
  Duracao INT NOT NULL,
  CanalID FOREIGN KEY REFERENCES Canal(CanalId)
);