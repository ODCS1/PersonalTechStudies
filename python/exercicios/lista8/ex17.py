# 17. Escreva uma função em Python recebe dois vetores de números como parâmetro. A
# função deverá retornar o vetor que se obtem da concatenação dos dois vetores dados.

def concatenar_vetores_for(vetor1: tuple[int], vetor2: tuple[int]) -> tuple[int]:
    if not isinstance(vetor1, tuple) or not isinstance(vetor2, tuple):
        raise ValueError("Os argumentos do parâmetro eram esperados como tuplas de inteiros!")

    novo_vetor = ()
    for num in vetor1:
        novo_vetor += (num,)
    for num in vetor2:
        novo_vetor += (num,)
    return novo_vetor

def concatenar_vetores_while(vetor1: tuple[int], vetor2: tuple[int]) -> tuple[int]:
    if not isinstance(vetor1, tuple) or not isinstance(vetor2, tuple):
        raise ValueError("Os argumentos do parâmetro eram esperados como tuplas de inteiros!")

    novo_vetor = ()
    i = 0
    while i < len(vetor1):
        novo_vetor += (vetor1[i],)
        i += 1
    
    j = 0
    while j < len(vetor2):
        novo_vetor += (vetor2[j],)
        j += 1

    return novo_vetor

def main():
    try:
        vetor1 = (1, 2, 3)
        vetor2 = (4, 5, 6)
        print(f"FOR: {concatenar_vetores_for(vetor1, vetor2)}")
        print(f"WHILE: {concatenar_vetores_while(vetor1, vetor2)}")
    except ValueError as e:
        print(f"[ERRO] {e}")

if __name__ == "__main__":
    main()
