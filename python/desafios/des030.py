# Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

num = int(input('Digite um número inteiro: '))

if num % 2 == 0:
    print('O {} é par!.'.format(num))
else:
    print('O {} é ímpar!'.format(num))