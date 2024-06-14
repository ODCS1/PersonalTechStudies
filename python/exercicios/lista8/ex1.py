# 1. Escreva uma função em Python que resulte a soma dos elementos de um vetor de números 
# dado. Faça um programa para testar sua função. - TUPLA


def calcular_soma_for(t: tuple[int]):      
    if not(isinstance(t, tuple)):
        raise ValueError

    soma = 0
    for i in range(len(t)):
            soma += t[i]
    return soma


def calcular_soma_while(t: tuple[int]):      
    if not(isinstance(t, tuple)):
        raise ValueError

    soma = 0
    contador = 0
    while contador < len(t):
         soma += t[contador]
         contador += 1
    return soma
        


def main():
    try:
        t = (1, 7, 11, 45, 8)
        c = []
        print(f"FOR: {calcular_soma_for(t)}")
        print(f"WHILE: {calcular_soma_while(t)}")
    except:
        print("[Erro] Passe uma tupla")

main()