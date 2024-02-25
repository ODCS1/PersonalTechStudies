-- BACKUP DATABASE

BACKUP DATABASE nomeDataBase
TO DISK = 'C:\arquivos\nomeDataBase.bak'
WITH FORMAT -- OPCIONAL
GO

A Linha opcional WITH FORMAT, formata o disco antes de gravar os dados.