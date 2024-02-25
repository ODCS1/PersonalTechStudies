nome = 'Guanabara'

cores = {'limpa':'\033[m', 
         'vermelho':'\033[31m', 
         'verde':'\033[32m', 
         'amarelo':'\033[33m', 
         'azul':'\033[34m', 
         'roxo':'\033[35m', 
         'azulclaro':'\033[36m', 
         'cinza':'\033[37m'}

print('Olá! Muito prazer em te conhecer, \033[4;31m{}\033[m!!!'.format(nome))