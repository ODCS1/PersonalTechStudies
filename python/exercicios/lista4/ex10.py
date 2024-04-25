# 10. Escreva um programa em Python que exiba na tela quantas vezes um dado número ocorre 
# em um lista de números fornecido

lista = [3, 6, 7, 1, 2 ,1, 5, 1]
alvo = 1

contador = 0
for i in range(len(lista)):
    if lista[i] == alvo:
        contador += 1

print(f"O valor {alvo}, aparece {contador} vezes na lista.")
