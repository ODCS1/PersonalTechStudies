# 22. Escreva uma função em Python que resulte a razão entre a média aritmética dos elementos 
# da diagonal principal e a média dos elementos da diagonal secundária de uma dada matriz 
# quadrada de números. Faça um programa para testar sua função.

def media_aritmetica_diagonal_principal(matriz: tuple[tuple[float]]) -> float:
    soma = 0.0
    n = len(matriz)
    for i in range(n):
        soma += matriz[i][i]
    return soma / n

def media_aritmetica_diagonal_secundaria(matriz: tuple[tuple[float]]) -> float:
    soma = 0.0
    n = len(matriz)
    for i in range(n):
        soma += matriz[i][n - 1 - i]
    return soma / n

def razao_media_diagonais(matriz: tuple[tuple[float]]) -> float:
    media_principal = media_aritmetica_diagonal_principal(matriz)
    media_secundaria = media_aritmetica_diagonal_secundaria(matriz)
    return media_principal / media_secundaria

def main():
    try:
        matriz = (
            (1.0, 2.0, 3.0),
            (4.0, 5.0, 6.0),
            (7.0, 8.0, 9.0)
        )
        print(f"Razão entre médias das diagonais: {razao_media_diagonais(matriz)}")
    except ValueError as e:
        print(f"[ERRO] {e}")

if __name__ == "__main__":
    main()
