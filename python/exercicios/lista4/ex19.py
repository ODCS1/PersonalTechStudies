# 19. Escreva um programa em Python para remover todas as ocorrências de um certo número 
# dado de um lista de números fornecida.


lista = [1, 2, 3, 4, 5, 1, 1, 5, 1]
alvo = 1


posicaoAnterior = -1
encontrou = False
procurando = True


i = len(lista) - 1
while i > -1:
    if lista[i] == alvo and procurando:
        procurando = False
        encontrou = True

    if encontrou and i == len(lista) - 1:
        lista.pop()
        encontrou = False
        procurando = True
    
    elif encontrou:
        posicaoAnterior = i
        lista[i] = lista[i + 1]
        i += 2

    i -= 1

print(lista)