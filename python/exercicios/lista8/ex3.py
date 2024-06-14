# 3. Escreva uma função em Python que resulte o maior elemento de um vetor de números 
# dado. Faça um programa para testar sua função


def maior_for(t: tuple[int]) -> int:
    if not(isinstance(t, tuple)):
        raise ValueError
    
    maior = t[0]
    for i in range(1, len(t)):
        if t[i] > maior:
            maior = t[i]
    return maior



def maior_while(t: tuple[int]) -> int:
    if not(isinstance(t, tuple)):
        raise ValueError
    
    maior = t[0]
    contador = 1
    while contador < len(t):
        if t[contador] > maior:
            maior = t[contador]
        contador += 1

    return maior
        

def main():
    try:
        t = (1, 2, 3, 4, 5)
        print(f"FOR: {maior_for(t)}")
        print(f"WHILE: {maior_while(t)}")
    except:
        print("[ERRO] O ARGUMENTO DO PARÂMETRO ERA ESPERADO UMA TUPLA!")


main()