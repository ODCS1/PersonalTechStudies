n1 = float(input('Digite um número: '))
n2 = float(input('Agora digite outro número: '))

if n1 == n2:
    print('Não existe valor maior, os dois são iguais.')
elif n1 > n2:
    print('O 1° valor digitado ({}) é maior.'.format(n1))
else:
    print('O 2° valor digitado ({}) é maior.'.format(n2))