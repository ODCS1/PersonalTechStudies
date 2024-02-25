# Escreva um programa que leia a velocidade de um carro.
# 
# Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
# 
# A multa vai custar R$7,00 por cada Km acima do limite.

velocidade = float(input('Digite a velocidade: '))

vel_Acim = velocidade - 80
multa = vel_Acim * 7

if velocidade > 80:
    print('Você passou com {}km/h, o limite é 80km/h, ou seja, \nvocê ultrapassou {}km/h o Limite de velocidade. \nPor isso será multado em R${} reais.'.format(velocidade, vel_Acim, multa))
else:
    print('Parabéns, você respeitou o limite de velocidade com {}km/h.'.format(velocidade))