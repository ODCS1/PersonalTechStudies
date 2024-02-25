# Faça im programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

from math import sin,cos,tan
angulo = float(input('Digite um ângulo em graus: '))


print('O sen {}° = {}\nO cos {}° = {}\nA tg {}° = {}'.format(angulo, sin(angulo), angulo, cos(angulo), angulo, tan(angulo)))