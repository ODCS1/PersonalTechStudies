# Faça um programa que leia três números e mostre qual é o maior e qual é menor.

n1 = float(input('Digite o 1°número: '))
n2 = float(input('Digite o 2°número: '))
n3 = float(input('Digite o 3°número: '))

if n1 > n2 and n1 > n3 and n2 > n3:
    print('{} é o maior número e {} é o menor.'.format(n1, n3))
elif n1 > n2 and n1 > n3 and n3 > n2:
    print('{} é o maior número e {} é o menor.'.format(n1, n2))
elif n2 > n1 and n2 > n3 and n1 > n3:
    print('{} é o maior número e {} é o menor.'.format(n2, n3))
elif n2 > n1 and n2 > n3 and n3 > n1:
    print('{} é o maior número e o {} é o menor.'.format(n2, n1))
elif n3 > n1 and n3 > n2 and n1 > n2:
    print('{} é o maior número e o {} é o menor.'.format(n3, n2))
elif n3 > n1 and n3 > n2 and n2 > n1:
    print('{} é o maior número e o {} é o menor.'.format(n3, n1))