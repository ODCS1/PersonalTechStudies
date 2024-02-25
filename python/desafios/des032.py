# Faça um programa que leia um ano bissexto qualquer e mostre se ele é BISSEXTO.

ano = int(input('Digite um ano para eu informar se ele é ou não um ano bissexto: '))

if ano % 4 == 0:
    print(f'{ano} é um ano bissexto...')
else:
    print(f'{ano} não é um ano bissexto...')