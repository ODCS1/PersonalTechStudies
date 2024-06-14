# 6. Escreva uma função em Python que resulte True, se todos os elementos de um vetor de 
# números dado forem par, ou False, caso contrário. Faça um programa para testar sua 
# função.


def todos_elementos_par_for(t: tuple[int]) -> bool:
    if not(isinstance(t, tuple)):
        raise ValueError
    
    for i in range(len(t)):
        if t[i] % 2 != 0:
            return False
    
    return True

def todos_elementos_par_while(t: tuple[int]) -> bool:
    if not(isinstance(t, tuple)):
        raise ValueError
    
    
    contador = 0
    while contador < len(t):
        if t[contador] % 2 != 0:
            return False
        contador += 1
    
    return True
        

def main():
    try:
        t = (4, 2, 6, 4, 8)
        t2 = (10, 2, 32, 4, 56, 6, 7, 8)
        print(f"FOR: {todos_elementos_par_for(t)}")
        print(f"WHILE: {todos_elementos_par_while(t2)}")
    except:
        print("[ERRO] O ARGUMENTO DO PARÂMETRO ERA ESPERADO UMA TUPLA!")

main()

