# 92. Escreva em Python uma função que resulta o inverso de uma dada lista de números. Faça 
# um programa para testar sua função.


def listaInversa(arr):
    listaSaida = [None] * len(arr)
    for i in range(len(listaSaida)):
        listaSaida[i] = arr[(-1) * (i + 1)]
    
    return listaSaida



def programa():
    lista = [1,2,3,4,5,6]
    listaRetorno = listaInversa(lista)
    print(f"Lista original: {lista} \nLista Inversa: {listaRetorno}")



programa()