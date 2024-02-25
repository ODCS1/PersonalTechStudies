print('-'*20)
print('|{:^18}|'.format('IMC'))
print('-'*20)

altura = float(input('Digite a altura(m): '))
peso = float(input('Agora o peso(kg): '))

imc = peso/(altura**2)

if imc < 18.5:
    print('Resultado = IMC: {:.2f} - Abaixo do Peso.'.format(imc))
elif imc >= 18.5 and imc < 25:
    print('Resultado = IMC: {:.2f} - Peso ideal.'.format(imc))
elif imc >= 25 and imc < 30:
    print('Resultado = IMC: {:.2f} - Sobrepeso.'.format(imc))
elif imc >= 30 and imc < 40:
    print('Resultado = IMC: {:.2f} - Obesidade.'.format(imc))
else: # último caso imc > 40
    print('Resultado = IMC: {:.2f} - Obesidade Mórbida.'.format(imc))
