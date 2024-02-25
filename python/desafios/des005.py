# Faça um programa que leia um número e mostre na tela o seu sucessor e seu antecessor.

num = int(input('Digite um número inteiro: '))
ant = num - 1
suc = num + 1
print('O antecessor de {} é {}.'.format(num, ant))
print('O sucessor de {} é {}.'.format(num,suc))