# Ex 3 - RA: 23505
from random import randint
# vetor = [0] * 5 

# user = int(input('Qual valor máximo para uma posição do vetor: '))

# for i in range(len(vetor)):
#     vetor[i] = randint(0, user)

# print(vetor)


# Leitura do número N informado pelo usuário
n = int(input("Digite um número inteiro positivo: "))

# Criação do vetor com 5 posições e preenchimento com valores aleatórios
vetor = [randint(0, n) for i in range(5)]

# Exibição do vetor original
print("Vetor original:", vetor)

# Inversão do vetor sem uso de vetor auxiliar
for i in range(len(vetor)//2):
    j = len(vetor) - 1 - i
    vetor[i], vetor[j] = vetor[j], vetor[i]

# Exibição do vetor invertido
print("Vetor invertido:", vetor)
