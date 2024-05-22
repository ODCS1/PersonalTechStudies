# 21. Escreva um programa em Python para remover de um lista de números dado todas as 
# ocorrências de uma certa seqüência de números em um outro lista de números que 
# também sera fornecido.

lista = [1, 2, 3, 7, 1, 2, 5, 1, 2, 3, 4, 1, 2, 3, 9, 1, 2, 3, 11]
sequencia = [1, 2, 3]

posicaoAtualLista = 0
posicaoAtualSequencia = 0
contadorSequencia = 0

while posicaoAtualLista < len(lista):
    if lista[posicaoAtualLista]  == sequencia[posicaoAtualSequencia]:
        contadorSequencia += 1
        posicaoAtualSequencia += 1

    else:
        posicaoAtualSequencia = 0
        contadorSequencia = 0
    
    if contadorSequencia == 3 and posicaoAtualLista != len(lista):
        lista.pop(posicaoAtualLista)
        lista.pop(posicaoAtualLista - 1)
        lista.pop(posicaoAtualLista - 2)
        posicaoAtualLista -= 3

        contadorSequencia = 0
        posicaoAtualSequencia = 0

    elif contadorSequencia == 3 and posicaoAtualLista == len(lista):
        lista.pop()
        lista.pop()
        lista.pop()

        break

        
    posicaoAtualLista += 1



print(lista)