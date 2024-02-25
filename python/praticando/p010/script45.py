nota1 = float(input('1° nota: '))
nota2 = float(input('2° nota: '))
m = (nota1 + nota2)/2

if m <= 4.9:
    print('REPROVADO!')
elif m >= 5 and m <= 6.9:
    print('RECUPERAÇÃO!')
else:
    print('APROVADO!')