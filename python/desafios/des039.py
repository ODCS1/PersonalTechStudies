# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade:
# 
# - Se ele ainda vai se alistar no serviço militar.
# - Se é a hora de se alistar.
# - Se já passou do tempo do alistamento.
# 
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

ano_na = int(input('Ano de nascimento: '))
ano = 2023

idade = ano - ano_na

if idade < 18:
    print('Você ainda vai se alistar...')
    temp = 18 - idade
    print('{} anos ainda faltam para você se alistar...')
elif idade == 18:
    print('Está na hora de você se alistar...')
else:
    print('O seu alistamento já passou.')
    temp = idade - 18
    print('{} anos já se passaram do seu alistamento.')

