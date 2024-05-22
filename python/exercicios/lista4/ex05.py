# 5. Escreva um programa em Python que exiba na tela quantos elementos de um lista de 
# números dado estão abaixo da média dos elementos do mesmo lista.

lista = [1,5,7,8,3]

soma = 0

for i in range(len(lista)):
    soma += lista[i]

media = soma / len(lista)

contador = 0
for j in range(len(lista)):
    if lista[j] < media:
        contador += 1

print(f"Media dos elementos da lista: {media} \nQuantidade de elementos abaixo da media: {contador}")