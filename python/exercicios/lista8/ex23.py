# 23. Escreva uma função em Python que resulte o maior elemento da diagonal secundária de 
# uma matriz quadrada de números. Faça um programa para testar sua função.

def maior_elemento_diagonal_secundaria(matriz: tuple[tuple[float]]) -> float:
    maior_elemento = matriz[0][len(matriz) - 1]
    for i in range(len(matriz)):
        elemento = matriz[i][len(matriz) - 1 - i]
        if elemento > maior_elemento:
            maior_elemento = elemento
    return maior_elemento

def main():
    try:
        matriz = (
            (1.0, 2.0, 3.0),
            (4.0, 5.0, 6.0),
            (7.0, 8.0, 9.0)
        )
        print(f"Maior elemento da diagonal secundária: {maior_elemento_diagonal_secundaria(matriz)}")
    except ValueError as e:
        print(f"[ERRO] {e}")

if __name__ == "__main__":
    main()
