# 24. Escreva uma função em Python que resulte o menor elemento de uma dada matriz 
# quadrada de números. Faça um programa para testar sua função.

def menor_elemento_matriz(matriz: tuple[tuple[float]]) -> float:
    menor_elemento = matriz[0][0]
    for linha in matriz:
        for elemento in linha:
            if elemento < menor_elemento:
                menor_elemento = elemento
    return menor_elemento

def main():
    try:
        matriz = (
            (5.0, 2.0, 3.0),
            (4.0, 9.0, 6.0),
            (7.0, 8.0, 1.0)
        )
        print(f"Menor elemento da matriz: {menor_elemento_matriz(matriz)}")
    except ValueError as e:
        print(f"[ERRO] {e}")

if __name__ == "__main__":
    main()
