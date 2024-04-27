# 18. Escreva um programa em Python para remover a ocorrência mais à direita de um certo 
# número dado de um lista de números fornecida


lista = [1, 5, 4, 5, 1, 2 , 3, 8]
alvo = 1


encontrou = False
contadorParaAlvo = 0


i = len(lista) - 1
while i > -1:
    if lista[i] == alvo and contadorParaAlvo == 0:
        contadorParaAlvo = 1
        encontrou = True

    if encontrou and i == (len(lista) - 1):
        break

    if encontrou:
        lista[i] = lista[i+1]
        i += 2

    i -= 1
        
    


lista.pop()

print(f"RESULTADO: {lista}")