# 23. Escreva um programa em Python que inverta um dado lista de números.

lista = [145, 542, 76, 38, 31]

listaInvertida = []


for i in range(len(lista)-1, -1, -1):
    listaInvertida.append(lista[i])


print(f"Lista original: {lista} \nLista invertida: {listaInvertida}")