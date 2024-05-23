# 93. Escreva uma função em Python que resulte a soma dos elementos de uma dada matriz de 
# úmeros reais. Faça um programa para testar sua função.

def somaElementosMatriz(matriz):
    soma = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            soma += matriz[i][j]

    return soma



def programa():
    matrizOriginal = [
        [1,2,0,3],
        [6,3,1,0],
        [0,2,0,1]
    ]

    somaElementos = somaElementosMatriz(matrizOriginal)

    print(f"A soma dos elementos da matriz é igual a: {somaElementos}")



programa()