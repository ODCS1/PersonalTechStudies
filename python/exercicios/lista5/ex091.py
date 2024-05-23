# 91. Escreva em Python uma função que resulta a concatenação de uma dada lista de números.
# Faça um programa para testar sua função

# IMPORTO List da biblioteca "typing"
from typing import List


# AQUI NO MÉTODO "concatenar" É RECEBIDO "arr" QUE COMO DESCRITO A DIREITA, É UMA LISTA DE INTEIROS.
# DEPOIS DO PARÊNTESES TEM UMA SETINHA COM "List[int]", INDICANDO O TIPO DE DADO QUE ESSA FUNÇÃO RETORNA.
def concatenar(arr: List[int]) -> List[int]:
    listaSecundaria: List[int] = [5,6,7,8,9]
    listaSaida = arr + listaSecundaria

    return listaSaida


def programa():
    lista = [1,2,3,4]
    listaConcatenada = concatenar(lista)
    print(f"Lista Original: {lista} \nLista Concatenada: {listaConcatenada}")

programa()