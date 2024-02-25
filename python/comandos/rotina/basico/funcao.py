# Função é uma rotina que obrigatoriamente retorna um valor

# As funções vinheram para modularizar o nosso código retornando valores, assim o formato procedural se torna não escalável, já que o programador é obrigado a escrever linha a linha, assim tomando tempo e dinheiro dentro de qualquer projeto.

# Script básico de uma função

def funcao():
    # Código ...
    return 'É função!!!'

# chamada da função
frase = funcao()

print(frase)

# O parênteses serve para passar valores, chamados de parâmetros, já que funções possuem um escopo local, ou seja, informações definidas dentro da função, são reconhecidas apenas dentro da função. Aí que vema passagem de parâmetro.