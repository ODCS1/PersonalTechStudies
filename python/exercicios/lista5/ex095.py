# 95. Escreva uma função em Python que resulte a média geométrica dos elementos de uma 
# dada matriz de números. Faça um programa para testar sua função.

from math import pow



# VERIFIQUE O LINK A SEGUIR PARA VER COMO CALCULAR A MÉDIA GEOMÉTRICA
# https://mundoeducacao.uol.com.br/matematica/media-geometrica.htm


def calcularMediaGeometrica(m):
    qtdElementosTotal = len(m)

    produtoElementos = 1
    for i in range(qtdElementosTotal):
        qtdElementosLista = len(m[i])
        for j in range(qtdElementosLista):
            produtoElementos *= m[i][j]

    mg = pow(produtoElementos, 1/qtdElementosTotal)
    return mg



def programa():

    matriz = [
        [4],
        [9]
    ]

    # matriz = [
    #     [1,2,3],
    #     [4,5,6],
    #     [7,8,9]
    # ]
    
    valorMediaGeometricaMatriz = calcularMediaGeometrica(matriz)
    print(f"Valor media geometrica Matriz: {valorMediaGeometricaMatriz}")


programa()
