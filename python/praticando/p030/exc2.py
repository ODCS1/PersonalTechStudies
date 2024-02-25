# 2 - Fatorial: Escreva um programa que calcule o fatorial de um número inteiro não negativo.


def fatorial(n):
    result = 1
    for i in range(1,n+1):
        result *= i

    return result


while True:
    num = input("Digite um número Natural: ")

    if (num.isdigit()):
        break

num = int(num)
print(f"O fatorial de {num} é {fatorial(num)}.")