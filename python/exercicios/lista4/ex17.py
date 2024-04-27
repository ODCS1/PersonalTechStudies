# 17. Escreva um programa em Python para remover a ocorrência mais à esquerda de um certo 
# número dado de um lista de números fornecida


# FORMA RESUMIDA
lista = [5, 4, 1, 5, 2 , 1, 8]
alvo = 1

lista.remove(alvo)
print(f"RESUMIDO:       {lista}")

lista = [5, 4, 1, 5, 2 , 1, 8]

# UTILIZANDO LÓGICA PRÓPRIA
encontrou = False
contadorParaAlvo = 0

for i in range(len(lista)):
    if lista[i] == alvo and contadorParaAlvo == 0:
        contadorParaAlvo += 1
        encontrou = True

    if encontrou and i < len(lista) - 1:
        lista[i] = lista[i+1]
    


lista.pop()

print(f"LÓGICA PRÓPRIA: {lista}")