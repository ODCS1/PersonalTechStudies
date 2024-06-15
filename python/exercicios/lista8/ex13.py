# 13. Escreva uma função em Python que resulte quantas vezes um dado vetor de números 
# contem um dos números de um vetor de números também fornecido. Faça um programa 
# para testar sua função.

def contar_ocorrencias_for(vetor_grande: tuple[int], vetor_pequeno: tuple[int]) -> int:
    if not isinstance(vetor_grande, tuple) or not isinstance(vetor_pequeno, tuple):
        raise ValueError
    
    count = 0
    for num in vetor_pequeno:
        for elem in vetor_grande:
            if elem == num:
                count += 1
    return count

def contar_ocorrencias_while(vetor_grande: tuple[int], vetor_pequeno: tuple[int]) -> int:
    if not isinstance(vetor_grande, tuple) or not isinstance(vetor_pequeno, tuple):
        raise ValueError
    
    count = 0
    i = 0
    while i < len(vetor_pequeno):
        j = 0
        while j < len(vetor_grande):
            if vetor_grande[j] == vetor_pequeno[i]:
                count += 1
            j += 1
        i += 1
    return count

def main():
    try:
        vetor_grande = (1, 2, 3, 4, 5, 2, 3, 4, 5, 2, 3, 4, 5)
        vetor_pequeno = (2, 3)
        print(f"FOR: {contar_ocorrencias_for(vetor_grande, vetor_pequeno)}")
        print(f"WHILE: {contar_ocorrencias_while(vetor_grande, vetor_pequeno)}")
    except ValueError as e:
        print(f"[ERRO] {e}")

if __name__ == "__main__":
    main()

