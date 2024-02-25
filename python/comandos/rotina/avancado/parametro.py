# Existem dois tipos principais de passagem de parâmetros em Python: passagem por valor e passagem por referência.

# 1 - Passagem por valor: Nesse caso, uma cópia do valor é passada para a função. Isso significa que quaisquer alterações feitas dentro da função não afetarão o valor original fora dela. Tipos primitivos, como números inteiros, números de ponto flutuante e strings, são passados por valor.

# Exemplo de passagem por valor:

def alterar_valor(numero):
    numero = 10

valor = 5
alterar_valor(valor)
print(valor)  # Saída: 5


# 2 - Passagem por referência: Nesse caso, é passada uma referência ao objeto ou estrutura de dados para a função. Isso significa que as alterações feitas dentro da função afetarão o objeto original fora dela. Tipos compostos, como listas e dicionários, são passados por referência.

# Exemplo de passagem por referência:

def alterar_lista(lista):
    lista.append(4)

minha_lista = [1, 2, 3]
alterar_lista(minha_lista)
print(minha_lista)  # Saída: [1, 2, 3, 4]


# É importante notar que embora seja possível modificar um objeto mutável dentro de uma função, como no exemplo acima, se você atribuir um novo objeto a uma variável de referência dentro da função, isso não afetará o objeto original fora dela.

# Exemplo:

def alterar_lista2(lista):
    lista.append(4)
    lista = [1, 2, 3]

lista = [0]
alterar_lista2(minha_lista)
print(minha_lista)  # Saída: [0, 4]


# Além disso, é possível definir parâmetros opcionais com valores padrão. Isso permite que você chame uma função sem especificar todos os argumentos, usando os valores padrão predefinidos.

# Exemplo de parâmetros opcionais:

def saudacao(nome, saudacao="Olá"):
    print(saudacao + ", " + nome)

saudacao("João")  # Saída: Olá, João
saudacao("Maria", "Oi")  # Saída: Oi, Maria


# Outras formas: 

# 1 - Passagem de parâmetros por nome: Em Python, você pode chamar uma função especificando explicitamente o nome dos parâmetros e seus valores correspondentes. Isso permite que você forneça os argumentos fora de ordem, desde que você especifique seus nomes.

# Exemplo de passagem de parâmetros por nome:

def saudacao2(nome, saudacao):
    print(saudacao + ", " + nome)

saudacao2(saudacao="Oi", nome="Maria")  # Saída: Oi, Maria


# 2 - Número variável de argumentos: Em algumas situações, pode ser útil definir uma função que possa aceitar um número variável de argumentos. O Python oferece duas formas para isso: parâmetros arbitrários posicionais e parâmetros arbitrários de palavras-chave.

# * Parâmetros arbitrários posicionais: Você pode definir um parâmetro na forma de *args para permitir que a função receba um número variável de argumentos posicionais. Esses argumentos são agrupados em uma tupla dentro da função.

# Exemplo de parâmetros arbitrários posicionais:

def somar(*args):
    total = 0
    for num in args:
        total += num
    return total

print(somar(1, 2, 3))  # Saída: 6
print(somar(4, 5, 6, 7))  # Saída: 22

# Outro exemplo: 

def concatenar(*args):
    resultado = ""
    for arg in args:
        resultado += arg
    return resultado

print(concatenar("Olá", ", ", "como", "vai", "você?"))  # Saída: Olá, como vai você?



# * Parâmetros arbitrários de palavras-chave: Você pode definir um parâmetro na forma de **kwargs para permitir que a função receba um número variável de argumentos de palavras-chave. Esses argumentos são agrupados em um dicionário dentro da função.

# Exemplo de parâmetros arbitrários de palavras-chave:

def mostrar_informacoes(**kwargs):
    for chave, valor in kwargs.items():
        print(f"{chave}: {valor}")

mostrar_informacoes(nome="João", idade=30, cidade="São Paulo")
# Saída:
# nome: João
# idade: 30
# cidade: São Paulo

# Mais um exemplo utilizando posicional e de palavras-chave:

def exibir_dados(*args, **kwargs):
    for arg in args:
        print(arg)
    for chave, valor in kwargs.items():
        print(chave + ": " + valor)

exibir_dados("Olá", "mundo", nome="João", idade="30")
# Saída:
# Olá
# mundo
# nome: João
# idade: 30


# 3 - Desempacotamento de argumentos: Em vez de passar os argumentos para uma função explicitamente, você também pode desempacotar uma sequência (como uma lista ou tupla) ou um dicionário e passá-los como argumentos separados usando o operador * ou **.

# Exemplo de desempacotamento de argumentos:

def somar2(a, b, c):
    return a + b + c

valores = [1, 2, 3]
print(somar2(*valores))  # Saída: 6

informacoes = {"a": 4, "b": 5, "c": 6}
print(somar2(**informacoes))  # Saída: 15