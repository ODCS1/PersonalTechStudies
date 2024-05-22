# 4. Escreva um programa em Python que exiba na tela o menor elemento de um lista de 
# números dado.

# DE FORMA MAIS RESUMIDA
lista = [1,5,7,8,3]

menorNumero = min(lista)
print("Resumida: " + str(menorNumero))

# USANDO LÓGICA PRÓPRIA
menorNumero2 = lista[0]

for i in range(1, len(lista)):
    if lista[i] < menorNumero2:
        menorNumero2 = lista[i]

print("Usando lógica: " + str(menorNumero2))