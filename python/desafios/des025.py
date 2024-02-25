# Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

nome = str(input('Digite o nome: ')).title()
dividido = nome.split()

if 'Silva' in dividido:
    print('O seu nome possuí Silva no nome.')
else:
    print('O seu nome não possuí Silva no nome.')