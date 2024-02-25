# 3 - Verificação de Número Primo: Crie um programa que determine se um número é primo ou não

def ehPrimo(n):
    cont = 0
    for i in range(1, n+1):
        if n % i == 0:
            cont +=1
    
    if cont > 2:
        return False
    else:
        return True

n = int(input("Digite um número natural: "))

print(f"É primo: {ehPrimo(n)}")