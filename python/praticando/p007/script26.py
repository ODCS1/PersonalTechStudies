# EXERCÍCIO 4

soma = 0
c = 1
while c <= 3:
    idade = int(input('Digite a idade: '))
    soma += idade
    c += 1

media = soma / 3

print(f'A média de idades é {media}')