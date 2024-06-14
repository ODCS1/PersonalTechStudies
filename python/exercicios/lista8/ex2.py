# 2. Escreva uma função em Python que resulte a média dos elementos de um vetor de 
# números dado. Faça um programa para testar sua função


def calcular_media_for(t: tuple[int]):
    if not(isinstance(t, tuple)):
        raise ValueError
    
    soma = 0
    for numero in t:
        soma += numero
    media = soma / len(t)
    return media

def calcular_media_while(t: tuple[int]):
    if not(isinstance(t, tuple)):
        raise ValueError
    
    soma = 0
    contador = 0
    while contador < len(t):
        soma += t[contador]
        contador += 1

    media = soma / len(t)
    return media
        

def main():
    try:
        t = (1, 2, 3, 4, 5)
        print(f"FOR: {calcular_media_for(t)}")
        print(f"WHILE: {calcular_media_while(t)}")
    except:
        print("[ERRO] O ARGUMENTO DO PARÂMETRO ERA ESPERADO UMA TUPLA!")


main()