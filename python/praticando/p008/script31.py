# Menu para interação do usuário com o sistema

def mensagem(msg):
  print(msg)
  input('Pressione <ENTER> para continuar ...')

def mostraMenu():
  print('**** CADASTRO DE CLIENTES ****\n')
  print('1. Novo Registro')
  print('2. Alterar um Registro')
  print('3. Deletar um Registro')
  print('4. Pesquisar\n')
  print('0. SAIR\n')


def trataOpcao(opcao):
  match opcao:
    case 1:
      mensagem('Incluir')
    case 2:
      mensagem('Alterar')
    case 3:
      mensagem('Deletar')
    case 4:
      mensagem('Pesquisa')
    case _:
      mensagem('Opção Inválida')


# if opcao == 1:
#   mensagem('Incluir')
# elif opcao == 2:
#   mensagem('Alterar')
# elif opcao == 3:
#   mensagem('Deletar')
# elif opcao == 4:
#   mensagem('Pesquisa')
# else:
#   mensagem('Opção Inválida')


while True:
  mostraMenu()
  op = int(input('Digite uma opção: '))
  if op == 0: break
  trataOpcao(op)