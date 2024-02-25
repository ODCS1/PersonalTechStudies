# Crie um programa que leia o nome completo de uma pessoa e mostre: 
# > O nome com todas as letras maiúsculas.
# > O nome com todas minúsculas.
# > Quantas letras ao todo (sem considerar espaços).
# > Quantas letras tem o primeiro nome. 

nome = input('Digite o seu nome completo: ')

print('Nome com todas letras maiúsculas: ', nome.upper())
print('Nome com todas letras minúsculas: ', nome.lower())

no_Space = nome.replace(' ', '')
print(f'O seu nome possuí {len(no_Space)} letras.')

dividido = nome.split()
print(f'O seu primeiro nome possuí {len(dividido[0])} letras.')
