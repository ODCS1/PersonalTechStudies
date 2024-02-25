# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

preco = float(input('Digite o valor do produto: '))
ajustep = preco - preco*(5/100)

print('O novo valor com 5% de desconto é R${:.2f} reais.'.format(ajustep))