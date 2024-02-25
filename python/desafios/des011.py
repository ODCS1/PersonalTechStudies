# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m^(2)

largura = float(input('Qual é a largura da parede: '))
altura = float(input('Qual é a altura da parede: '))
areap = largura * altura
qttinta = areap / 2

print('Para pintar uma parede com {}m de largura e {}m de altura (area: {}m^2), será nescessário {:.2f}l de tinta'.format(largura, altura, areap, qttinta))