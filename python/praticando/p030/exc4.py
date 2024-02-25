# 1 - Fibonacci: Escreva um programa para gerar os primeiros n termos da sequência de Fibonacci.

def fibonacci(n):
    anterior1 = 1
    anterior2 = 0
    atual = 1

    strFibo = ""
    strFibo += str(anterior2) + ' '
    strFibo += str(anterior1)
    for i in range(1, n - 1):
        strFibo += ' ' + str(atual)
        anterior2 = anterior1
        anterior1 = atual
        atual = anterior1 + anterior2
    
    return strFibo


n = int(input("Digite um número natural: "))

print(f"O fibonacci de {n} é: \n{fibonacci(n)}")