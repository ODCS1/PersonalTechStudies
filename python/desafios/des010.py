# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar. 
# Considerando:
# US$1,00 = R$3,27

dreais = float(input('Quantos reais possuí na carteira: '))
ddol = dreais / 3.27

print('Com R${} reais, você pode comprar US${:.2f} dólares.'.format(dreais, ddol))