# 7. Escreva um programa em Python para verificar se um dado lista de números está em 
# ordem crescente, exibe na telando True em caso afirmativo, ou False, caso contrário.

lista = [1,5,7,8,10]
estaCrescente = True

valorAnterior = lista[0]
for i in range(1, len(lista), 1):
    if valorAnterior > lista[i]:
        estaCrescente = False
    
    valorAnterior = lista[i]


print(f"Está crescente: {estaCrescente}")