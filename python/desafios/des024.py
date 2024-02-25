# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".

cidade = str(input('Nome da cidadde: ')).title()
dividido = cidade.split()
if dividido[0] == 'Santo':
    print('Essa cidade começa com a palavra Santo.')
else:
    print('Essa cidade não começa com a palavra Santo.')