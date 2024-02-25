# 5 - Contagem de Vogais: Crie um programa que conte o número de vogais em uma frase fornecida pelo usuário. Ignore letras maiúsculas/minúsculas.

cont = 0

vogal = ['a', 'e', 'i', 'o', 'u']

frase = input("Digite algo: ").lower()

for i in range(len(vogal)):
    for j in range(len(frase)):
        if vogal[i] == frase[j]:
            cont += 1


print(cont)