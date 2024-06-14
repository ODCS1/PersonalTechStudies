# 10. Escreva uma função em Python que resulte quantas vezes um dado número ocorre em um 
# vetor de números fornecido. Faça um programa para testar sua função.


def contar_ocorrencias_for(numero: int, vetor: tuple[int]) -> int:
    if not isinstance(vetor, tuple):
        raise ValueError("O segundo argumento deve ser uma tupla de números.")
    
    count = 0
    for num in vetor:
        if num == numero:
            count += 1
    return count


def contar_ocorrencias_while(numero: int, vetor: tuple[int]) -> int:
    if not isinstance(vetor, tuple):
        raise ValueError("O segundo argumento deve ser uma tupla de números.")
    
    count = 0
    i = 0
    while i < len(vetor):
        if vetor[i] == numero:
            count += 1
        i += 1
    return count

def main():
    try:
        t = (1, 2, 3, 4, 3, 5)
        n = 3
        print(f"FOR: {contar_ocorrencias_for(n, t)}")
        print(f"WHILE: {contar_ocorrencias_while(n, t)}")
    except ValueError as e:
        print(f"[ERRO] {e}")

if __name__ == "__main__":
    main()
