n1 = int(input('Digite o 1° número: '))
n2 = int(input('Digite o 2° número: '))
n3 = int(input('Digite o 3° número: '))
n4 = int(input('Digite o 4° número: '))

if n1 > n2 and n1 > n3 and n1 > n4:
    print('O {} é o maior valor colocado.'.format(n1))
elif n2 > n1 and n2 > n3 and n1 > n4:
    print('O {} é o maior valor colocado.'.format(n2))
elif n3 > n1 and n3 > n2 and n3 > n4:
    print('O {} é o maior valor colocado.'.format(n3))
elif n4 > n1 and n4 > n2 and n4 > n3:
    print('O {} é o maior valor colocado.'.format(n4))

