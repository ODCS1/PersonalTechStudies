# 18. Escreva em Python uma função que resulta o inverso de um dado vetor de números. Faça
# um programa para testar sua função.

def inverter_vetor_for(vetor: tuple[int]) -> tuple[int]:
    if not isinstance(vetor, tuple):
        raise ValueError("O argumento do parâmetro era esperado uma tupla!")

    novo_vetor = ()
    for i in range(len(vetor) - 1, -1, -1):
        novo_vetor += (vetor[i],)
    return novo_vetor

def inverter_vetor_while(vetor: tuple[int]) -> tuple[int]:
    if not isinstance(vetor, tuple):
        raise ValueError("O argumento do parâmetro era esperado uma tupla!")

    novo_vetor = ()
    i = len(vetor) - 1
    while i >= 0:
        novo_vetor += (vetor[i],)
        i -= 1
    return novo_vetor

def main():
    try:
        vetor = (1, 2, 3, 4, 5)
        print(f"FOR: {inverter_vetor_for(vetor)}")
        print(f"WHILE: {inverter_vetor_while(vetor)}")
    except ValueError as e:
        print(f"[ERRO] {e}")

if __name__ == "__main__":
    main()
