# Praticando um pouco alguns conceitos gerais

# 1 - 
# a = 'String sendo teste'
# b = a.split('s')
# print(a, b)

# 2 - 
# a = 'String'.lower()
# print(a)

# 3 - 
# s = 'teste de outrora'
# print(s[::-1])

# 4 -
# print('Este valor: %10.4f' %122.144)
# print('A: %10.4f'%122.144)

# 5 - 
# print('Testando formatação... \nnúmero: %s \nString: %s'%(10.37850973753, 'É string'))
# print('Testando formatação... \nnúmero: %r \nString: %r'%(10.37850973753, 'É string'))

# 6 - 
# print('First: %s \nSecond: %1.2f \nThird: %r'%('String', 3.14, 15))
# %s para string
# %num1.num2f para float, sendo num1 a quantidade de espaços a esquerda e num2 a quantidade de cassas de números após a vírgula.
# %r para números iteiros

# 7 - 
# print('Testando {n} texto{pl}{v} onde o format está sendo utilizado{p} Assim eu posso manipular o meu print{i}'.format( v=',', p='.', i='!', n=1, pl='s'))

# 8 - 
# num = 3.2
# frase = f'Possuo uma frase e %.4f!'%(num)
# print(frase)

# 9 - 
# num = 3.2
# frase = 'Possuo uma frase'
# frase2 = frase + '%6.3f'%(num) + '!'
# print(frase)
# print(frase2)

# 10 -
# my_dictionary = {
#     '1': 'Primeiro',
#     '2': [1,'um'],
#     '3': 'cinco'
# }

# print(my_dictionary['2'][0])
