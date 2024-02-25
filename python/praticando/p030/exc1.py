# 1 - Soma de Dois Números: Escreva um programa que receba dois números como entrada e exiba a soma deles.

def soma(a, b):
    return a + b

a = int(input("Digite um inteiro: "))
b = int(input("Digite um segundo inteiro: "))

print(f"A soma entre {a} e {b} é {soma(a, b)}.")