# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
# 
# O programa deverá escrever na tela se o usuário venceu ou perdeu.
from os import system as sy
from random import randint

numero_Sorteado = randint(0, 5)
print('-'*40)
print('|{}{:^38}{}|'.format('\033[31m', 'ADIVINHA', '\033[m'))
print('-'*40)
print('OPÇÕES: >> 0 >> 1 >> 2 >> 3 >> 4 >> 5 <<')
n = int(input('Faça sua escolha: '))

if numero_Sorteado == n:
  print('VOCÊ VENCEU...')
else:
  print('VOCÊ PERDEU... O valor sorteado foi o {}.'.format(numero_Sorteado))