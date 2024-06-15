# 15. Escreva uma função em Python que resulte a posição mais a direita de uma dada seqüência 
# de números presente num vetor de números dado em um outro vetor (maior) de números 
# que será fornecido. Faça um programa para testar sua função.

def posicao_direita_sequencia_for(sequencia: tuple[int], vetor: tuple[int]) -> int:
    if not isinstance(sequencia, tuple) or not isinstance(vetor, tuple):
        raise ValueError("O argumento do parâmetro era esperado uma tupla!")
    
    len_seq = len(sequencia)
    posicao = -1
    for i in range(len(vetor) - len_seq + 1):
        if vetor[i:i+len_seq] == sequencia:
            posicao = i
    return posicao

def posicao_direita_sequencia_while(sequencia: tuple[int], vetor: tuple[int]) -> int:
    if not isinstance(sequencia, tuple) or not isinstance(vetor, tuple):
        raise ValueError("O argumento do parâmetro era esperado uma tupla!")
    
    len_seq = len(sequencia)
    posicao = -1
    i = 0
    while i < len(vetor) - len_seq + 1:
        if vetor[i:i+len_seq] == sequencia:
            posicao = i
        i += 1
    return posicao

def main():
    try:
        vetor_grande = (1, 2, 3, 4, 5, 2, 3, 4, 5)
        sequencia = (2, 3)
        print(f"FOR: {posicao_direita_sequencia_for(sequencia, vetor_grande)}")
        print(f"WHILE: {posicao_direita_sequencia_while(sequencia, vetor_grande)}")
    except ValueError as e:
        print(f"[ERRO] {e}")

main()
