# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# 
# - À vista dinheiro/cheque:10% de desconto
# - À vista no cartão:5% de desconto
# - Em até 2x no cartão:Preço normal
# - 3x ou mais no cartão:20% de juros

valor = float(input('Digite o valor: '))
c_Pagamento = int(input('Para cartão à vista digite [1] \nPara cartão em até 2x digite [2] \nPara cartão em 3x ou mais digite [3] \nPara dinheiro ou cheque digite [4] \nDigite a opção de pagamento: '))

match c_Pagamento:
    case 1:
        valor -= valor * 5/100
    case 2:
        valor = valor
    case 3:
        valor += valor * 20/100
    case 4:
        valor -= valor * 10/100


# if c_Pagamento == 1:
#     valor -= valor * 5/100
# elif c_Pagamento == 2:
#     valor = valor
# elif c_Pagamento == 3:
#     valor += valor * 20/100
# elif c_Pagamento == 4:
#     valor -= valor * 10/100

print('O valor ficou R${} reais, de acordo com as condições de pagamento.'.format(valor))