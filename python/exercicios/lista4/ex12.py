# 12. Escreva um programa em Python que exiba na tela a posição mais a direita de uma dado 
# lista de números que contem um dos números de um lista de números também fornecido.

def posicao_mais_a_direita(lista_numeros, numeros_procurados):
    posicao = -1
    numerosEncontrados = 0

    for numero_procurado in numeros_procurados:
        if numero_procurado in lista_numeros:
            numerosEncontrados += 1
            
        
        if numerosEncontrados == len(numeros_procurados):
            posicao = lista_numeros.index(numero_procurado)
            break
        
    return posicao


lista_numeros = [1, 3, 5, 7, 9, 3, 2, 4, 11]
numeros_procurados = [1, 5, 11]
posicao = posicao_mais_a_direita(lista_numeros, numeros_procurados)
print("A posição mais à direita é:", posicao)