from math import pow as p

opcao = 0
while opcao != 2:
  print('-'*30)
  print('|{:^28}|'.format('Calculadora de IMC'))
  print('|{:^28}|'.format('1 - Calcular o IMC'))
  print('|{:^28}|'.format('2 - Sair'))
  print('-'*30)
  opcao = int(input('Digite a opção: '))
  if opcao == 2:
    print('Saindo...')
  else:
    altura = float(input('Digite a sua altura(m): '))
    peso = float(input('Digite o seu peso(kg): '))

    imc = peso / p(altura,2)

    if imc == 0:
      print('Digite uma opção válida.')
    else:
      if imc <= 18.5:
          print('\n\tSituação: abaixo do peso.\n')
      elif imc > 18.5 and imc <= 25:
          print('\n\tSituação: Peso normal.\n')
      elif imc > 25 and imc <= 30:
          print('\n\tSituação: acima do peso.\n')
      elif imc > 30:
          print('\n\tSituação: Obesidade.\n')