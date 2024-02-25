# Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos de uma Sequência de Fibinacci.
# 
# 0 -> 1 -> 1 -> 2 -> 3 -> 5 -> 8 


while True:
    n = input("Digite um número inteiro: ")

    if n.isnumeric():
        n = int(n)
        break
    else:
        print("DIGITE UM VALOR VÁLIDO!")


print(0, end='')
atual = 1
anterior1 = atual
print(" -> " + str(atual), end='')

for i in range(1, n-1):
    anterior2 = anterior1
    anterior1 = atual
    print(" -> " + str(anterior1), end='')
    atual = anterior1 + anterior2
