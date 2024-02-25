# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

n1 = float(input('Digite a 1° nota: '))
n2 = float(input('Digite a 2° nota do aluno: '))
m = (n1 + n2)/2
print('A média entre as notas {} e {} foi de {:.1f}'.format(n1,n2,m))