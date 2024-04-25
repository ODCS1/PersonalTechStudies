# 3. Escreva um programa em Python que exiba na tela o maior elemento de um lista de 
# números dado.

# DE FORMA MAIS RESUMIDA
lista = [1,5,7,8,3]

maiorNumero = max(lista)
print("Resumida: " + str(maiorNumero))

# USANDO LÓGICA PRÓPRIA
maiorNumero2 = lista[0]

for i in range(1, len(lista)):
    if lista[i] > maiorNumero2:
        maiorNumero2 = lista[i]

print("Usando lógica: " + str(maiorNumero2))