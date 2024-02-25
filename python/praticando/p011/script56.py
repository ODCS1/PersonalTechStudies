# Praticando função no python

from os import system as sy

def mostrar():
    sy('cls')
    print('-' * 40)
    print('|{}{:^38}{}|'.format('\033[31m', 'CALCULANDO', '\033[m'))
    print('-' * 40)
    

def calcular(numeros):
    # mostrar()
    soma = 0
    sub = 0
    i = 0
    while i < len(numeros):
        soma += numeros[i]
        sub -= numeros[i]
        i += 1
    return f'A soma total: {soma} \nA subtração total: {sub}'


def user():
    mostrar()
    nome = input('Nome: ')
    mostrar()
    print('Para parar digite 0')

    numeros = []
    while True:
        pos = len(numeros) + 1
        numeros.append(int(input(f'Digite o {pos}° número: ')))

        # Colocando a restrição
        if numeros[len(numeros) - 1] == 0:
            numeros.pop(len(numeros) - 1)
            break

    print(f'{nome}, a sua lista com os valores armazenados: {numeros}')
    print(calcular(numeros))
    
user()