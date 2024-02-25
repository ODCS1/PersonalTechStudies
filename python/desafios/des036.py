# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# 
# Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.

valor_casa = float(input('Digite o valor da casa: '))
salario = float(input('Digite o salário: '))
qt_meses = int(input('Quanos anos deseja pagar: ')) * 12

valor_prestacao = valor_casa / qt_meses

if valor_prestacao > (30/100) * salario:
    print('Não é possível fazer o empéstimo com as informações colocadas...')
else:
    print('Parabéns!!! O seu empréstimo foi aprovado.')