nome = str(input('Nome: '))
idade = int(input('Idade: '))
gen = str(input('Genêro[m/f]: '))
te = int(input('Tempo de empresa: '))

if gen == 'm':
    if idade > 18 and te < 5:
        print('{} possuí 50 créditos para receber.'.format(nome))
    elif te >= 5 and te < 10 and idade > 18:
        print('{} possuí 100 créditos para receber.'.format(nome))
    elif te >= 10 and idade > 18:
        print('{} possuí 200 créditos para receber.'.format(nome))
    else:
        print('Menor de idade não possuí créditos a retirar.')
else:
    if idade > 18 and te < 5:
        print('{} possuí 50 créditos para receber.'.format(nome))
    elif te >= 5 and te < 10 and idade > 18:
        print('{} possuí 100 créditos para receber.'.format(nome))
    elif te >= 10 and idade > 18:
        print('{} possuí 200 créditos para receber.'.format(nome))
    else:
        print('Menor de idade não possuí créditos a retirar.')
