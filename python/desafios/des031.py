# Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 para viagens mais longas

dist = float(input('Distância[km]: '))

if dist <= 200:
    valor_Passagem = dist * 0.5
else:
    valor_Passagem = dist * 0.45

print('Com a distância de {}km, a passagem vai custar R${} reais.'.format(dist, valor_Passagem))