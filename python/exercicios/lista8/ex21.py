# 21. Escreva uma função em Python que resulte a média geométrica dos elementos de uma 
# dada matriz de números. Faça um programa para testar sua função.

import math

def media_geometrica_matriz_for(matriz: tuple[tuple[float]]) -> float:
    produto = 1.0
    total_elementos = 0
    for linha in matriz:
        for elemento in linha:
            produto *= elemento
            total_elementos += 1
    return math.pow(produto, 1 / total_elementos)

def media_geometrica_matriz_while(matriz: tuple[tuple[float]]) -> float:
    produto = 1.0
    total_elementos = 0
    i = 0
    while i < len(matriz):
        j = 0
        while j < len(matriz[i]):
            produto *= matriz[i][j]
            total_elementos += 1
            j += 1
        i += 1
    return math.pow(produto, 1 / total_elementos)

def main():
    try:
        matriz = (
            (1.0, 2.0, 4.0),
            (8.0, 16.0, 32.0),
            (64.0, 128.0, 256.0)
        )
        print("FOR: {:.2f}".format(media_geometrica_matriz_for(matriz)))
        print("WHILE: {:.2f}".format(media_geometrica_matriz_while(matriz)))
    except ValueError as e:
        print(f"[ERRO] {e}")

if __name__ == "__main__":
    main()
