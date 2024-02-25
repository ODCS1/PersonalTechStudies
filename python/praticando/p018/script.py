idade = int(input('Idade: '))

if idade < 18:
    sm = 'Preparando...'
elif idade == 18:
    sm = 'Deve ser realizado.'
else:
    sm = 'Se ainda não realizado, regularize.'

print('Situação: {}.'.format(sm))