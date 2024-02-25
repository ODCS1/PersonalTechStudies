# Ex 1 - RA: 23505
from random import randint

vetor = [0] * 50
maior_valor = 0
for i in range(len(vetor)):
    vetor[i] = randint(0, 20)
    if maior_valor < vetor[i]:
        maior_valor = vetor[i]

posição = []
soma = 0
QTD_num9 = 0

for i in range(len(vetor)):
    soma += vetor[i]
    if vetor[i] == 9:
        QTD_num9 += 1   
    if vetor[i] == maior_valor:
        posição.append(i)  

    

print(f'VETOR: \n{vetor}. \nSoma dos valores armazenados no vetor: {soma} \nNúmero de ocorrências do valor 9: {QTD_num9} \nMaior valor armazenado no vetor: {maior_valor} \nPosições onde aparece o MAIOR valor encontrado: {posição}')