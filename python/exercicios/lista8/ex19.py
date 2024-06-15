# 19. Escreva uma função em Python que resulte a soma dos elementos de uma dada matriz de 
# números reais. Faça um programa para testar sua função.

def soma_elementos_matriz_for(matriz: tuple[tuple[float]]) -> float:
    soma = 0.0
    for linha in matriz:
        for elemento in linha:
            soma += elemento
    return soma

def soma_elementos_matriz_while(matriz: tuple[tuple[float]]) -> float:
    soma = 0.0
    i = 0
    while i < len(matriz):
        j = 0
        while j < len(matriz[i]):
            soma += matriz[i][j]
            j += 1
        i += 1
    return soma

def main():
    try:
        matriz = (
            (1.5, 2.5, 3.5),
            (4.5, 5.5, 6.5),
            (7.5, 8.5, 9.5)
        )
        print(f"FOR: {soma_elementos_matriz_for(matriz)}")
        print(f"WHILE: {soma_elementos_matriz_while(matriz)}")
    except ValueError as e:
        print(f"[ERRO] {e}")

if __name__ == "__main__":
    main()
