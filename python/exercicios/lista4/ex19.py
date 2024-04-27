# 19. Escreva um programa em Python para remover todas as ocorrências de um certo número 
# dado de um lista de números fornecida.


lista = [1, 2, 3, 4, 5, 1, 1, 5]
alvo = 1
ocorrencias = 0


for i in range(len(lista)):
    if lista[i] == alvo and i < len(lista) - 1:
        for j in range(i , len(lista)):
            lista[i] = lista[i+1]
        lista.pop()
        ocorrencias += 1

    if i == len(lista) - 1:
        pass


# for j in range(ocorrencias):
#     lista.pop()


print(lista)