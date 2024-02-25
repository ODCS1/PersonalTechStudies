# Ex 2 - RA: 23505
from random import randint

vetor = [0] * 10

for i in range(len(vetor)):
    vetor[i] = randint(0, 20)
vetor2 = vetor.copy()



for i in range(len(vetor2)):
    vetor2[i] = vetor[i-1]

print(vetor)
print(vetor2)