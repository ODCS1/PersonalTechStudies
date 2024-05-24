# 94. Escreva uma função em Python que resulte a soma dos elementos da diagonal principal de 
# uma dada matriz quadrada de números. Faça um programa para testar sua função.

def somaElementosDiagonalPrincipalMatriz(m):
    soma = 0

    for i in range(len(m)):
        soma += m[i][i]

    return soma


def programa():
    matriz = [
        [1, 52345, 52345],
        [52345, 1, 52345],
        [52345, 52345, 1]
    ]
    somaElementos = somaElementosDiagonalPrincipalMatriz(matriz)

    print(f"A soma dos elementos da diagonal principal da matriz: {somaElementos}")


programa()