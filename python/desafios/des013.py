# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

sal = float(input('Digite o valor do seu salário: '))

novosal = sal + sal*(15/100)

print('O seu novo salário com 15% de aumento é {:.2f}.'.format(novosal))
