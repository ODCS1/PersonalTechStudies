# 16. Escreva uma função em Python que resulte quantas vezes um dado vetor de números 
# contem uma seqüência de números em um outro vetor (menor) de números que será 
# fornecido. Faça um programa para testar sua função.


def contar_sequencia_for(sequencia: tuple[int], vetor: tuple[int]) -> int:
    if not isinstance(sequencia, tuple) or not isinstance(vetor, tuple):
        raise ValueError
    
    len_seq = len(sequencia)
    count = 0
    for i in range(len(vetor) - len_seq + 1):
        if vetor[i:i+len_seq] == sequencia:
            count += 1
    return count

def contar_sequencia_while(sequencia: tuple[int], vetor: tuple[int]) -> int:
    if not isinstance(sequencia, tuple) or not isinstance(vetor, tuple):
        raise ValueError
    
    len_seq = len(sequencia)
    count = 0
    i = 0
    while i < len(vetor) - len_seq + 1:
        if vetor[i:i+len_seq] == sequencia:
            count += 1
        i += 1
    return count

def main():
    try:
        vetor_grande = (1, 2, 3, 4, 5, 2, 3, 4, 5, 2, 3)
        sequencia = (2, 3)
        print(f"FOR: {contar_sequencia_for(sequencia, vetor_grande)}")
        print(f"WHILE: {contar_sequencia_while(sequencia, vetor_grande)}")
    except ValueError as e:
        print(f"[ERRO] {e}")

main()
