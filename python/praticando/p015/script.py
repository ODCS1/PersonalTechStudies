print('-'*20)
print('|{:^18}|'.format('Passagem Ônibus'))
print('-'*20)

dist = float(input('Qual distância você vai percorrer: '))

if dist <= 200:
    preco = dist * 0.5
else:
    preco = dist * 0.4

print('O preço fica em R${} reais.'.format(preco))