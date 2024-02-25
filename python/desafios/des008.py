# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

metros = float(input('Digite uma distância considerando estar em metros: '))
centi = metros * (1/100)
mili = metros * (1/1000)
print('A distância {}m, convertida para centímetros e milímetros respectivamente, foram {:.2f} e {:.3f}.'.format(metros,centi,mili))