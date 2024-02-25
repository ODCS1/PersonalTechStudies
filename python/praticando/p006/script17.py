n = int(input('Digite um número inteiro: '))

divi = 0
for cont in range(1, n+1):
    print(cont)
    if n % cont == 0:
        divi += 1

if divi > 2 or n == 0:
    print(f'O número {n}, não é um número primo.')
    if n != 0:
        print('{} é o número de divisores do {}.'.format(divi, n))
else:
    print('{} é o número de divisores do {}.'.format(divi, n))
    print(f'O número {n}, é um número primo.')