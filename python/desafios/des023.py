# Faça um  programa que leia um número de 0 a 9999 e mostre na tela cada um dos digitos separados.
# Ex:
# Digite um número: 1834
# 
# unidade: 4
# dezena: 3
# centena: 8
# milhar: 1

num = str(input('Digite um número de no máximo unidade de milhar: '))
n = int(num)
num = num.split()
if n > 9999 or n < 1000: 
    print('Escolha um número válido!!!')
else:
    print(f'unidade: {num[0][3]} \ndezena: {num[0][2]} \ncentena: {num[0][1]} \nmilhar: {num[0][0]}')


# Ou também poderia ser feito desta forma, utilizando a matemática:
# 
# num = int(input('Digite um número de no máximo unidade de milhar: '))
# u = num // 1 % 10
# d = num // 10 % 10
# c = num // 100 % 10
# m = num // 1000 % 10
# print(f'unidade: {u} \ndezena: {d} \ncentena: {c} \nmilhar: {m}')