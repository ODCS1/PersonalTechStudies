
res = 's'
while res == 's':
    print('Olá, seja bem vindo!')
    nome = input('Qual é o seu nome: ')
    ano_nasc = int(input('Qual ano você nasceu: '))
    idade = 2023 - ano_nasc

    if idade < 5:
        print('Olá!')
    elif idade < 10:
        print('Oi!')
    elif idade < 15:
        if idade % 2 == 0:
            print('PAR!')
        else:
            print('ÍMPAR!')
    else:
        print('Sim!')