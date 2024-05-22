# 13. Escreva um programa em Python que exiba na tela quantas vezes um dado lista de 
# números contem um dos números de um lista de números também fornecido

from random import randint as rd

lista = [1,3,5,1,6,1]
elementos = [1,2,6,9]

posicaoAleatoria = rd(0, len(elementos))

contador = 0
for i in range(len(lista)):
    if lista[i] == elementos[posicaoAleatoria]:
        contador += 1

print(f"O elemento {elementos[posicaoAleatoria]} aparece {contador} vezes!")

