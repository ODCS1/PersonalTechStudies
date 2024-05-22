# 22. Escreva um programa em Python recebe dois listas de números como parâmetro. A função 
# deverá retornar o lista que se obtem da concatenação dos dois listas dados.

def concatenar_duas_listas_exemplo1(a, b):
    return a+b


def concatenar_duas_listas_exemplo2(a, b):
    tamanhoTotal = len(a) + len(b)
    lista_retorno_exemplo1 = [None for _ in range(tamanhoTotal)]
    lista_retorno_exemplo2 = []
    pos_lista_b = 0

    for i in range(tamanhoTotal):
        if i < len(a):
            lista_retorno_exemplo1[i] = a[i]
            lista_retorno_exemplo2.append(a[i])
        else:
            lista_retorno_exemplo1[i] = b[pos_lista_b]
            lista_retorno_exemplo2.append(b[pos_lista_b])
            pos_lista_b += 1

    if lista_retorno_exemplo1 == lista_retorno_exemplo2:
        return lista_retorno_exemplo1
    else:
        return [-1]


lista1 = [1, 2, 3]
lista2 = [4, 5, 6]

lista3 = concatenar_duas_listas_exemplo1(lista1, lista2)
lista4 = concatenar_duas_listas_exemplo2(lista1, lista2)

print(lista3)
print(lista4)