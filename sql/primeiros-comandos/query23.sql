-- TIPOS DE DADOS

1. Boleanos
2. Caracteres
3. Números
4. Temporais

## 1. Boleano
Por padrão ele é inicializado com nulo, e pode receber tanto 1 ou 0.
Bit

## 2. Caracteres
Tamanho fixo - char
-- Permite inserir até uma quantidade fixa de caracteres e sempre ocupa todo o espaço reservado

Tamanhos variáveis - varchar ou nvarchar
-- Permite inserir até uma quantidade que for definida, porém só usa o espaço qe for preenchido

## 3. Números
### Valores Exatos

1. TINYINT - Não tem parte fracionada(ex: 1.42, 26.23), somente 1, 123123, 32364, 436..

2. SMALLINT - Mesma coisa porém limite maior

3. INT - Mesma coisa porém limite maior

4. BIGINT - Mesma coisa porém limite maior

5. NUMERIC ou DECIMAL - Valores exatos, porém permite ter parte fracionada, que também pode ser especificado a precisão
e escala (escala é o número de dígitos na parte fracional) ex: NUMERIC(5,2) 113,44

### Valores Aproximados
1. REAL - Tem precisão aproximada de até 15 digítos
2. FLOAT - Mesmo conceito do REAL

## 4. Temporais
DATE - Armazena data no formato aaaa/mm/dd

DATETIME - Aramazena data e horas no formato aaaa/mm/dd/hh:mm:ss

DATETIME2 - Data e horas com adição de milisegundos no formato aaaa/mm/dd:hh:mm:sssssss

SMALLDATETIME - Data e hora, mas respeitando o limite entre '1900-01-01:00:00:00' até '2079-06-06:23:59:59'

TIME - Armazena horas, minutos, seguntos e milisegundos respeitando o limite de '00:00:00.0000000'

DATETIMEOFFSET - Permite armazenar informações de data e horas incluindo o fuso horário