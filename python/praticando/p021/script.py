curso = str(input('Faz algum curso aqui[s/n]: '))

if curso == 's':
    nome = str(input('Nome: '))
    ra = int(input('RA? '))
    print('Confirmado {}, o seu RA é o {}.'.format(nome,ra))
else:
    print('Você não pode acessar o nosso sistema, apenas alunos da nossa instituição podem ter acesso.')
