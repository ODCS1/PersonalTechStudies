# Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
# 
# - O primeiro valor é maior
# - O segundo valor é maior
# - Não existe valor maior, os dois são iguais.

n1 = int(input('Digite o 1° número: '))
n2 = int(input('Digite o 2°número: '))

if n1 > n2:
    print(f'{n1} é maior que {n2}.')
elif n2 > n1:
    print(f'{n2} é maior que {n1}.')
else:
    print('Não existe valor maior ou menor, os dois são iguais.')