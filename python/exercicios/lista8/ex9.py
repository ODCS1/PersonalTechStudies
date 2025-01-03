# 9. Escreva uma função em Python que resulte a posição mais a direita de um dado número 
# em um vetor de números. Faça um programa para testar sua função.


def posicao_direita_for(numero: int, vetor: tuple[int]) -> int:
    if not isinstance(vetor, tuple):
        raise ValueError
    
    posicao = -1
    for i in range(len(vetor)):
        if vetor[i] == numero:
            posicao = i
    return posicao

def posicao_direita_while(numero: int, vetor: tuple[int]) -> int:
    if not isinstance(vetor, tuple):
        raise ValueError
    
    posicao = -1
    i = 0
    while i < len(vetor):
        if vetor[i] == numero:
            posicao = i
        i += 1
    return posicao



def main():
    try:
        t = (51, 232, 232, 23, 4, 5743, 232)
        n = 232
        print(f"FOR: {posicao_direita_for(n, t)}")
        print(f"WHILE: {posicao_direita_while(n, t)}")
    except:
        print("[ERRO] O ARGUMENTO DO PARÂMETRO ERA ESPERADO UMA TUPLA!")

main()