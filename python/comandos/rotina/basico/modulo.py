# A modularização é muito parecido com uma função, a diferença está que o módulo não retorna nada para onde foi feita a chamada, ou seja, é simplesmente um bloco de códigos que se repete várias vezes dentro da estrutura geral do script e faz oq foi definido.

def impPar(a, b):
    if a % 2 == 0:
        print('a é par!')
    else:
        print('a é ímpar!')

    if b % 2 == 0:
        print('b é par!')
    else:
        print('b é ímpar!')


impPar(1, 3)

# Outro exemplo com uma verificação de número primo

def numPrim(x):
    contador_divisores = 0
    for i in range(1, x+1):
        if x % i == 0:
            contador_divisores += 1
    
    if contador_divisores > 2 and x != 0:
        print(f'{x} não é número primo!')
    elif contador_divisores == 2:
        print(f'{x} é um número primo!')
    else:
        print(f'{x} não é uma opção válida!')

num_user = int(input('Digite um inteiro positivo: '))
numPrim(num_user)