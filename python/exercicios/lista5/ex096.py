# 96. Escreva uma função em Python que resulte a razão entre a média aritmética dos elementos 
# da diagonal principal e a média dos elementos da diagonal secundária de uma dada matriz 
# quadrada de números. Faça um programa para testar sua função.


from typing import List


def calcular(m):
    ma_diagonal_principal = 0
    ma_diagonal_secundaria = 0
    
    soma = 0
    for i in range(len(m)):
        soma += m[i][i]
    



def programa():
    matriz = [
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ]

    res = calcular(matriz)





programa()