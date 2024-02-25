# Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# 
# - Equilátero: todos os lados iguais
# - Isóceles: dois lados iguais
# - Escaleno: todos os lados diferentes

print('Este programa vai te pedir 3 Segmentos de reta: ')

l1 = int(input('1° segmento de reta: '))
l2 = int(input('2° segmento de reta: '))
l3 = int(input('3° segmento de reta: '))

if l1 +  l2 > l3 and l1 + l3 > l2 and l2 + l3 > l1:
    print('Os 3 segmentos de reta formam um triângulo...')
    if l1 == l2 and l1 == l3:
        print('Tipo: Equilátero')
    elif l1 == l2 and l1 != l3 or l1 == l3 and l1 != l2 or l2 == l3 and l2 != l1:
        print('Tipo: Isóceles')
    else:
        print('Tipo: Escaleno')
else:
    print('Os 3 segmerntos de reta não formam um triângulo...')