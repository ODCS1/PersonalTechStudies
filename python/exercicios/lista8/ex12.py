# 12. Escreva uma função em Python que resulte a posição mais a direita de uma dado vetor de 
# números que contem um dos números de um vetor de números também fornecido. Faça 
# um programa para testar sua função.

def posicao_mais_a_direita_while(tupla_numeros: tuple[int], numeros_procurados: tuple[int]) -> int:
    if not (isinstance(tupla_numeros, tuple) and isinstance(numeros_procurados, tuple)):
        raise ValueError("Os argumentos do parâmetro eram esperados como tuplas de inteiros!")
    
    posicao = -1
    c = len(tupla_numeros) - 1
    while c >= 0:
        if tupla_numeros[c] in numeros_procurados:
            posicao = c
            break
        c -= 1
    return posicao

def posicao_mais_a_direita_for(tupla_numeros: tuple[int], numeros_procurados: tuple[int]) -> int:
    if not (isinstance(tupla_numeros, tuple) and isinstance(numeros_procurados, tuple)):
        raise ValueError("Os argumentos do parâmetro eram esperados como tuplas de inteiros!")
    
    posicao = -1
    for i in range(len(tupla_numeros) - 1, -1, -1):
        if tupla_numeros[i] in numeros_procurados:
            posicao = i
            break
    return posicao

def main():
    try:
        t = (1, 2, 3, 4, 3, 5)
        n = (3, 4, 3)
        print(f"FOR: {posicao_mais_a_direita_for(t, n)}")
        print(f"WHILE: {posicao_mais_a_direita_while(t, n)}")
    except ValueError as e:
        print(f"[ERRO] {e}")

if __name__ == "__main__":
    main()

