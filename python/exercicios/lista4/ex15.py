# 15. Escreva um programa em Python que exiba na tela a posição mais a direita de uma dada 
# seqüência de números presente num lista de números dado em um outro lista (maior) de 
# números que será fornecido.

lista = [1, 2, 7, 1, 2, 3, 81, 1, 2, 3, 1, 2, 3, 45, 1, 2, 10]
sequencia = [1, 2, 3]


posAtualSequencia, contadorSequenciaAtual, posFinalSequencia = 0, 0, 0


for i in range(len(lista)):
    if lista[i] == sequencia[posAtualSequencia]:
        contadorSequenciaAtual += 1
        posAtualSequencia += 1
    else:
        contadorSequenciaAtual, posAtualSequencia = 0, 0

    if contadorSequenciaAtual == len(sequencia):
        posAtualSequencia, contadorSequenciaAtual = 0, 0
        posFinalSequencia = max(posFinalSequencia, i)

print(f"Posição Final da sequência: {posFinalSequencia}")
