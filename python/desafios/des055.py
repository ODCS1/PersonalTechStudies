# Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

from os import system as sy

def formatar():
  sy('cls')
  print('-' * 40)
  print('|{}{:^38}{}|'.format('\033[31m', 'ANALISANDO', '\033[m'))
  print('-' * 40)


def ler():
    formatar()
    vet_peso = []
    for i in range(1, 6):
       peso_atual = float(input(f'Digite o {i}° peso: '))
       vet_peso.append(peso_atual)
    copiar(vet_peso)

def copiar(vet_peso):
   peso_orde = vet_peso.copy()
   peso_orde.sort()
   mostrar(peso_orde)

def mostrar(peso_orde):
   print(f'Maior peso: {peso_orde[len(peso_orde) - 1]} \nMenor peso: {peso_orde[0]}')

ler()