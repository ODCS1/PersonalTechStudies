# 20. Escreva uma função em Python que resulte a soma dos elementos da diagonal principal de 
# uma dada matriz quadrada de números. Faça um programa para testar sua função.

def soma_diagonal_principal_for(matriz: tuple[tuple[float]]) -> float:
    soma = 0.0
    for i in range(len(matriz)):
        soma += matriz[i][i]
    return soma

def soma_diagonal_principal_while(matriz: tuple[tuple[float]]) -> float:
    soma = 0.0
    i = 0
    while i < len(matriz):
        soma += matriz[i][i]
        i += 1
    return soma

def main_soma_diagonal_principal():
    try:
        matriz = (
            (1.0, 0.0, 0.0),
            (0.0, 2.0, 0.0),
            (0.0, 0.0, 3.0)
        )
        print(f"FOR: {soma_diagonal_principal_for(matriz)}")
        print(f"WHILE: {soma_diagonal_principal_while(matriz)}")
    except ValueError as e:
        print(f"[ERRO] {e}")

if __name__ == "__main__":
    main_soma_diagonal_principal()
