# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.

from math import hypot

ca = int(input('Digite o cateto adjacente: '))
co = int(input('Digite o cateto oposto: '))

print('A hipotenusa dos catetos {} e {} é {}.'.format(ca,co,hypot(ca,co)))