# Formas de passar um vetor  por parâmetro

# 1 - Passagem por valor:
# Nesse caso, uma cópia do vetor é passada para a função. Modificações feitas dentro da função não afetam o vetor original fora dela.

def modificar_vetor(vetor):
    vetor.append(4)

meu_vetor = [1, 2, 3]
modificar_vetor(meu_vetor[:])  # Passando uma cópia do vetor, também funcionaria meu_vetor.copy()
print(meu_vetor)  # Saída: [1, 2, 3]


# 2 - Passagem por referência:
# Nesse caso, a referência ao vetor é passada para a função. Modificações feitas dentro da função afetam diretamente o vetor original fora dela.


def modificar_vetor(vetor):
    vetor.append(4)
    vetor[0] = 100

meu_vetor = [1, 2, 3]
modificar_vetor(meu_vetor)
print(meu_vetor)  # Saída: [100, 2, 3, 4]


# 3 - Desempacotamento de vetor:
# É possível desempacotar os elementos de um vetor e passá-los como argumentos separados para uma função usando o operador *.

def somar(a, b, c):
    return a + b + c

valores = [1, 2, 3]
print(somar(*valores))  # Saída: 6


# 4 - Passagem de parâmetro arbitrário posicional (*args):
# Você pode usar a passagem de parâmetro arbitrário posicional para permitir que uma função receba um número variável de elementos do vetor.


def concatenar(*args):
    resultado = ""
    for arg in args:
        resultado += arg
    return resultado

meu_vetor = ["Olá", ", ", "mundo!"]
print(concatenar(*meu_vetor))  # Saída: Olá, mundo!


# Misturando o Descompactamento de vetor com passagem de parâmetro positional:

def concatenar_strings(*args):
    resultado = ""
    for arg in args:
        resultado += arg
    return resultado

vetor = ["Olá", ", ", "mundo!"]
outras_strings = "Como", "vai?"

print(concatenar_strings(*vetor, *outras_strings))  # Saída: Olá, mundo! Como vai?
