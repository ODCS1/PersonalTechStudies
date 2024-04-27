# 20. Escreva um programa em Python para remover todas as ocorrências dos números que 
# compõem a seqüência de números em um dado lista de números de um lista de números 
# (maior) que também será fornecido

lista = [1, 4, 1, 6, 5, 7, 1, 8]
sequencia = [1, 5 ,7, 8]

i = 0
while i < len(lista):
    if lista[i] in sequencia:
        lista.pop(i)
        i -= 1


    i += 1

print(lista)