n1 = int(input('Digite o 1° número: '))
n2 = int(input('Digite o 2° número: '))

print('Soma digite [soma]...\nSubtração digite [subt]...\nMultiplicação digite [multi]...\nDivisão digite [divi]...')
op = str(input('Escolha: ')).lower

if op == 'soma':
    print('Soma = {}'.format(n1 + n2))
elif op == 'subt':
    print('Subtração: {}.'.format(n1 - n2))
elif op == 'multi':
    print('Multiplicação: {}'.format(n1 * n2))
elif op == 'divi':
    if n2 != 0:
        print('Divisão: {}'.format(n1 / n2))
    else:
        print('Não existe divisão real por 0')
else:
    print('Opção inválida, porfavor escolha uma opção descrita acima.')
  