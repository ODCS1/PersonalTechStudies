# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raíz quadrada.

n = int(input('Digite um número inteiro: '))
dobro = n*2
triplo = n*3
raizq = n**0.5
print('O valor colocado foi {}, o seu dobro é {}, o triplo é {} e a sua raíz quadrada é {:.2f}.'.format(n,dobro,triplo,raizq))