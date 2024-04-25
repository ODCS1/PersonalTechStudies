# 1. Escreva um programa em Python que exiba na tela a soma dos elementos de um lista de números dado

lista = [1,5,7,8,3]


soma = 0
for i in range(len(lista)):
    soma += lista[i]

print(f"A soma dos elementos: {soma}")


