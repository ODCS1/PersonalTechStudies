print('-'*50)
print('|{:^48}|'.format('CALCULADORA'))
print('-'*50)
print('-Escrevendo um valor, será exibido a sua tabuada-\n')

valor = int(input('Digite o valor: '))

print('\n{:^50}'.format('- Resultado -'))
cont = 0
while cont <= 10:
    print('{} x {} = {}'.format(valor, cont, valor * cont))
    cont += 1

print('-'*50)
print('Encerrando...')
print('-'*50)