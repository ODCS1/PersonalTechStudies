# 7. Escreva uma função em Python para verificar se um dado vetor de números está em ordem 
# crescente, resultando True em caso afirmativo, ou False, caso contrário. Faça um 
# programa para testar sua função.


def ordem_crescente_for(t: tuple[int]) -> bool:
    if not isinstance(t, tuple):
        raise ValueError
    
    for i in range(len(t) - 1):
        if t[i] > t[i + 1]:
            return False
    return True

def ordem_crescente_while(t: tuple[int]) -> bool:
    if not isinstance(t, tuple):
        raise ValueError
    
    i = 0
    while i < len(t) - 1:
        if t[i] > t[i + 1]:
            return False
        i += 1
    return True


def main():
    try:
        t = (1, 2, 3, 4, 5)
        t2 = (1, 8, 2, 3, 4, 5)
        print(f"FOR: {ordem_crescente_for(t)}")
        print(f"WHILE: {ordem_crescente_while(t2)}")
    except:
        print("[ERRO] O ARGUMENTO DO PARÂMETRO ERA ESPERADO UMA TUPLA!")

main()