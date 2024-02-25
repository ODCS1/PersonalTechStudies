print('')
print('O programa vai pedir 3 segmentos de retas inteiro;')
print('')
print('E depois vai te informar se é possivel formar um triângulo com esses segmentos;')
print('')
print('Caso seja possível, ele vai te informar ainda qual o tipo desse triângulo com relação a medida de seus lados (Equilátero, isóceles, escaleno).')
print('')

s1 = int(input('Digite o 1° segmento de reta: '))
s2 = int(input('Digite o 2° segmento de reta: '))
s3 = int(input('Digite o 3° segmento de reta: '))

if s1 + s2 < s3 or s2 + s3 < s1 or s1 + s3 < s2:
    print('Não forma um triângulo!')
elif s1 + s2 > s3 and s2 + s3 > s1 and s1 + s3 > s2:
    print('Forma um triângulo')
    if s1 == s2 and s1 == s3:
        print('O triângulo é do tipo equilátero.')
    elif s1 == s2 and s1 != s3:
        print('O triângulo é do tipo isóceles.')
    elif s1 != s2 and s2 != s3 and s1 != s3:
        print('O triãngulo é do tipo escaleno.')