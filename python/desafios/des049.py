# Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

# (DEASAFIO 009) Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada.

num = int(input('Digiter um número: '))

for i in range(1, 11):
    print(f'{i} x {num} = {num * i}')