# 5. Escreva uma função em Python que resulte quantos elementos de um vetor de números 
# dado estão abaixo da média dos elementos do mesmo vetor. Faça um programa para testar 
# sua função
from ex2 import calcular_media_for, calcular_media_while

def abaixo_media_for(t: tuple[int]) -> int:
    media = calcular_media_for(t)

    contador = 0
    for j in range(len(t)):
        if t[j] < media:
            contador += 1

    return contador

def abaixo_media_while(t: tuple[int]) -> int:
    media = calcular_media_while(t)

    contador = 0
    i = 0
    while i < len(t):
        if t[i] < media:
            contador += 1
        i += 1
            
    return contador


def main():
    try:
        t = (1, 2, 3, 4, 5)
        print(f"MEDIA: {calcular_media_for(t)}")
        print(f"FOR: {abaixo_media_for(t)}")
        print(f"WHILE: {abaixo_media_while(t)}")
    except:
        print("[ERRO] O ARGUMENTO DO PARÂMETRO ERA ESPERADO UMA TUPLA!")
    
main()