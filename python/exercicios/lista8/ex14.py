# 14. Escreva uma função em Python que resulte a posição mais a esquerda de uma dada
# seqüência de números presente num vetor de números dado em um outro vetor (maior) de 
# números que será fornecido. Faça um programa para testar sua função.

def posicao_esquerda_sequencia_for(sequencia: tuple[int], vetor: tuple[int]) -> int:
    if not isinstance(sequencia, tuple) or not isinstance(vetor, tuple):
        raise ValueError
    
    len_seq = len(sequencia)
    for i in range(len(vetor) - len_seq + 1):
        if vetor[i:i+len_seq] == sequencia:
            return i
    return -1

def posicao_esquerda_sequencia_while(sequencia: tuple[int], vetor: tuple[int]) -> int:
    if not isinstance(sequencia, tuple) or not isinstance(vetor, tuple):
        raise ValueError
    
    len_seq = len(sequencia)
    i = 0
    while i < len(vetor) - len_seq + 1:
        if vetor[i:i+len_seq] == sequencia:
            return i
        i += 1
    return -1

def main():
    try:
        vetor_grande = (1, 2, 3, 4, 5, 2, 3, 4, 5)
        sequencia = (2, 3)
        print(f"FOR: {posicao_esquerda_sequencia_for(sequencia, vetor_grande)}")
        print(f"WHILE: {posicao_esquerda_sequencia_while(sequencia, vetor_grande)}")
    except ValueError as e:
        print(f"[ERRO] {e}")

main()
