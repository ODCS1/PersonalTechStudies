# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

num = int(input('Digite um número: '))

num_divi = 0
for i in range(1, num+1):
    if num % i == 0:
        num_divi += 1 
  
if num_divi > 2:
    print(f'Não é um número primo (possuí {num_divi} divisores) ...')
else:
    print(f'{num} é um número primo (possuí {num_divi} divisores) . . .')