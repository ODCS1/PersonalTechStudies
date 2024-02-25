opcao = 0
while opcao != 3:
    print('-'*40)
    print('\tOPERAÇÕES DISPONÍVEIS')
    print('-'*40)
    print('')
    print('\t1 = Listar todos os alunos')
    print('\t2 - Incluir um aluno')
    print('\t3 - Sair')
    print('')

    opcao = int(input('Digite uma opção: '))
    if opcao == 1:
        print('\t\tListar alunos.\n')
    elif opcao == 2:
        print('\t\tIncluir aluno.\n')
    elif opcao != 3:
        print('\t\tDigite uma opcao válida.\n')

print('\nEncerrando...')