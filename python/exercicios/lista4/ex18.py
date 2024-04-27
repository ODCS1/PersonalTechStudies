# 18. Escreva um programa em Python para remover a ocorrência mais à direita de um certo 
# número dado de um lista de números fornecida


lista = [1, 5, 4, 5, 2 , 1, 8]
alvo = 1


encontrou = False
contadorParaAlvo = 0

for i in range(len(lista)-1, -1, -1):
    if lista[i] == alvo and contadorParaAlvo == 0:
        contadorParaAlvo += 1
        encontrou = True

    if encontrou and i < len(lista) - 1:
        lista[i] = lista[i+1]
        break
    


lista.pop()

print(f"RESULTADO: {lista}")