# 1. Escreva uma função em Python que resulte a soma dos elementos de um vetor de números 
# dado. Faça um programa para testar sua função. - TUPLA


def resultado(t: tuple[int]):
        
    if not(isinstance(t, tuple)):
        raise ValueError
    

    soma = 0

    for i in range(len(t)):
            soma += t[i]
    
    return soma
        


def main():
    try:
        t = (1, 7, 11, 45, 8)
        c = []
        print(resultado(t))
    except:
        print("[Erro] Passe uma tupla")

main()