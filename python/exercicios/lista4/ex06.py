# 6. Escreva um programa em Python que exiba na tela True, se todos os elementos de um lista
# de números dado forem par, ou False, caso contrário.

lista = [1,5,7,8,3]
todosPar = True

for i in range(len(lista)):
    if lista[i] % 2 != 0:
        todosPar = False


print(f"Todos são pares: {todosPar}")
