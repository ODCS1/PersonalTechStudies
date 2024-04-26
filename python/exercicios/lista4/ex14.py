# 14. Escreva um programa em Python que exiba na tela a posição mais a esquerda de uma dada 
# seqüência de números presente num lista de números dado em um outro lista (maior) de 
# números que será fornecido.

lista = [93, 1, 2, 4, 1, 253, 36, 1, 2, 3, 325, 5, 23, 1, 2, 3]
sequencia = [1, 2, 3]

posInicialSequencia = len(lista)
posAtualSequencia, contadorSequenciaAtual = 0, 0


for i in range(len(lista)):
    if lista[i] == sequencia[0]:
        contadorSequenciaAtual += 1
        posAtualSequencia += 1
        posInicialSequencia = i
    elif lista[i] == sequencia[posAtualSequencia]:
        contadorSequenciaAtual += 1
        posAtualSequencia += 1
    else:
        contadorSequenciaAtual, posAtualSequencia = 0, 0

    if contadorSequenciaAtual == len(sequencia):
        break

print(f"Posição inicial da sequência: {posInicialSequencia}")