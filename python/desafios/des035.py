# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

print('Este programa vai te pedir 3 medidas, estas medidas são referentes a segmentos de retas, caso essas 3 medidas sejam possível formar um triângulo ou não, o sistema irá informar.')

l1 = int(input('1° segmento de reta: '))
l2 = int(input('2° segmento de reta: '))
l3 = int(input('3° segmento de reta: '))

if l1 +  l2 > l3 and l1 + l3 > l2 and l2 + l3 > l1:
    print('Os 3 segmentos de reta formam um triângulo...')
else:
    print('Os 3 segmerntos de reta não formam um triângulo...')