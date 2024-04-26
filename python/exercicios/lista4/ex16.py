# 16. Escreva um programa em Python que exiba na tela quantas vezes um dado lista de 
# números contem uma seqüência de números em um outro lista (menor) de números que 
# será fornecido

lista = [1, 2, 7, 1, 2, 3, 1, 2, 3, 81, 1, 2, 3, 1, 2, 3, 45, 1, 2, 10]
sequencia = [1, 2, 3]


contadorDeSequencias, contadorSequenciaAtual = 0, 0

for i in range(len(lista)):
    if lista[i] == sequencia[contadorSequenciaAtual]:
        contadorSequenciaAtual += 1
    else:
        contadorSequenciaAtual = 0
    
    if contadorSequenciaAtual == len(sequencia):
        contadorDeSequencias += 1
        contadorSequenciaAtual = 0

print(f"Sequência apareceu {contadorDeSequencias} vezes!")