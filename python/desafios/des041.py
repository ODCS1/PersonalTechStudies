# A confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria com a idade:
# 
# - Até 9 anos: MIRIM
# - Até 14 anos: INFANTIL
# - Até 19 anos: JUNIOR
# - Até 20 anos: SÊNIOR
# - Acima: MASTER

ano = int(input('Digite o ano: '))
 
ano_a = 2023
idade = ano_a - ano

if idade <= 9:
    print('Categoria: Mirim')
elif idade <= 14:
    print('Categoria: Infantil')
elif idade < 19:
    print('Categoria: Júnior')
elif idade < 20:
    print('Categoria: Sênior')
else:
    print('Categoria: Master')
    