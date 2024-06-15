# 25. Dadas duas matrizes de números de igual dimensão, escreva um procedimento em Python 
# que resulte a soma das duas. Faça um programa para testar sua função.

def soma_matrizes(matriz1: tuple[tuple[float]], matriz2: tuple[tuple[float]]) -> tuple[tuple[float]]:
    if len(matriz1) != len(matriz2) or len(matriz1[0]) != len(matriz2[0]):
        raise ValueError("As matrizes devem ter as mesmas dimensões.")
    
    n = len(matriz1)
    m = len(matriz1[0])
    resultado = []
    for i in range(n):
        linha_resultado = []
        for j in range(m):
            linha_resultado.append(matriz1[i][j] + matriz2[i][j])
        resultado.append(tuple(linha_resultado))
    return tuple(resultado)

def main():
    try:
        matriz1 = (
            (1.0, 2.0),
            (3.0, 4.0)
        )
        matriz2 = (
            (5.0, 6.0),
            (7.0, 8.0)
        )
        resultado = soma_matrizes(matriz1, matriz2)
        for linha in resultado:
            print(linha)
    except ValueError as e:
        print(f"[ERRO] {e}")

if __name__ == "__main__":
    main()
