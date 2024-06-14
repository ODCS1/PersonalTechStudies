# 8. Escreva uma função em Python que resulte a posição mais a esquerda de um dado número 
# em um vetor de números. Faça um programa para testar sua função


def posicao_esquerda_for(numero: int, vetor: tuple[int]) -> int:
    if not isinstance(vetor, tuple):
        raise ValueError
    
    for i in range(len(vetor)):
        if vetor[i] == numero:
            return i
    return -1

def posicao_esquerda_while(numero: int, vetor: tuple[int]) -> int:
    if not isinstance(vetor, tuple):
        raise ValueError
    
    i = 0
    while i < len(vetor):
        if vetor[i] == numero:
            return i
        i += 1
    return -1


def main():
    try:
        t = (51, 232, 232, 23, 4, 5743, 232)
        n = 232
        print(f"FOR: {posicao_esquerda_for(n, t)}")
        print(f"WHILE: {posicao_esquerda_while(n, t)}")
    except:
        print("[ERRO] O ARGUMENTO DO PARÂMETRO ERA ESPERADO UMA TUPLA!")

main()