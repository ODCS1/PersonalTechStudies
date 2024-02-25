while True:
  idade = int(input('Sua idade: '))
  
  if idade < 0:
    print('Sua idade não pode ser negativa. Digite novamente...')
  elif idade > 100:
    print('Por Favor, dirija-se para a arquibancada pois você não pode jogar.')
  else:
    break

end = input('Seu endereço: ')