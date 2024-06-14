# 4. Escreva uma função em Python que resulte o menor elemento de um vetor de números 
# dado. Faça um programa para testar sua função.

def menor_for(t: tuple[int]) -> int:
    if not(isinstance(t, tuple)):
        raise ValueError
    
    menor = t[0]
    for i in range(1, len(t)):
        if t[i] < menor:
            menor = t[i]
    return menor



def menor_while(t: tuple[int]) -> int:
    if not(isinstance(t, tuple)):
        raise ValueError
    
    menor = t[0]
    contador = 1
    while contador < len(t):
        if t[contador] < menor:
            menor = t[contador]
        contador += 1

    return menor
        

def main():
    try:
        t = (1, 2, 3, 4, 5)
        print(f"FOR: {menor_for(t)}")
        print(f"WHILE: {menor_while(t)}")
    except:
        print("[ERRO] O ARGUMENTO DO PARÂMETRO ERA ESPERADO UMA TUPLA!")


main()