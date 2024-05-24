# 93. Escreva uma função em Python que resulte a soma dos elementos de uma dada matriz de 
# úmeros reais. Faça um programa para testar sua função.

from typing import List

def somaElementosMatriz(matriz: List[List[int]]) -> int:
    soma: int = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            soma += matriz[i][j]

    return soma



def programa():
    matrizOriginal: List[int] = [
        [1,2,0,3],
        [6,3,1,0],
        [0,2,0,1]
    ]

    somaElementos: int = somaElementosMatriz(matrizOriginal)

    print(f"A soma dos elementos da matriz é igual a: {somaElementos}")



programa()