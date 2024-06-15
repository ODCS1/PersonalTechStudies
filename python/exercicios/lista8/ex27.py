# 27. Dadas duas matrizes de números (a quantidade de linhas da primeira deve ser igual à 
# quantidade de colunas da segunda e a quantidade de colunas da primeira deve ser igual à 
# quantidade de linhas da segunda), escreva uma função em Python que resulta a 
# multiplicação das duas. Faça um programa para testar sua função.

def multiplicacao_matrizes(matriz1: tuple[tuple[float]], matriz2: tuple[tuple[float]]) -> tuple[tuple[float]]:
    if len(matriz1[0]) != len(matriz2):
        raise ValueError("Número de colunas da primeira matriz deve ser igual ao número de linhas da segunda matriz.")
    
    n1 = len(matriz1)
    m1 = len(matriz1[0])
    n2 = len(matriz2)
    m2 = len(matriz2[0])
    
    resultado = []
    for i in range(n1):
        linha_resultado = []
        for j in range(m2):
            elemento = 0.0
            for k in range(n2):
                elemento += matriz1[i][k] * matriz2[k][j]
            linha_resultado.append(elemento)
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
        resultado = multiplicacao_matrizes(matriz1, matriz2)
        for linha in resultado:
            print(linha)
    except ValueError as e:
        print(f"[ERRO] {e}")

if __name__ == "__main__":
    main()
