print('-'*20)
print('|{:^18}|'.format('EMPRÉSTIMO'))
print('-'*20)

vc = float(input('Valor da casa: '))
sal = float(input('Salário: '))
tempo = int(input('Quantos anos para pagar: '))

parcela = vc / (tempo*12)

if parcela > sal*(30/100):
    print('Empréstimo não possível!')
else:
    print('Empréstimo possível de ser solicitado!')
    