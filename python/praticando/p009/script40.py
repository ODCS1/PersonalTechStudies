# jogo da velha
# Antonio Ilton - RA:23505

from os import system  as sy

# cores
cores = {'limpa':'\033[m', 
         'vermelho':'\033[31m', 
         'verde':'\033[32m', 
         'amarelo':'\033[33m', 
         'azul':'\033[34m', 
         'roxo':'\033[35m', 
         'azulclaro':'\033[36m', 
         'cinza':'\033[37m'}

# criando o tabuleiro
tabuleiro = [1,2,3,4,5,6,7,8,9]
vez_do_jogador = 1


# Cabeçalho do jogo
def inicio():
    print()
    print('-'*40)
    print('|{}{:^38}{}|'.format(cores["vermelho"], 'JOGO DA VELHA', cores['limpa']))
    print('-'*40)


# Mostrar o jogo
def mostraJogo(tabuleiro):

    sy('cls')
    inicio()
    for i in range(1, 10):
        match i:
            case 1:
                print(f'\t\t {tabuleiro[i-1]}', end='')      
            case 2:
                print(f' {tabuleiro[i-1]}', end='')
            case 3:
                print(f' {tabuleiro[i-1]}', end='')
            case 4:
                print(f'\t\t {tabuleiro[i-1]}', end='')
            case 5:
                print(f' {tabuleiro[i-1]}', end='')
            case 6:
                print(f' {tabuleiro[i-1]}', end='')
            case 7:
                print(f'\t\t {tabuleiro[i-1]}', end='')
            case 8:
                print(f' {tabuleiro[i-1]}', end='')
            case 9:
                print(f' {tabuleiro[i-1]}', end='')
        if (i in [3,6,9]): 
            print(f" ")
            if (i!=9): print("\t\t---+---+---")
        else:
            print(f" ", end='|')

# funcao para verificar se o jogador ganhou
def jogador_ganhou(letra):
    return (
    # linha superior
    (tabuleiro[0] == letra and tabuleiro[1] == letra and tabuleiro[2] == letra) or
    # linha do meio
    (tabuleiro[3] == letra and tabuleiro[4] == letra and tabuleiro[5] == letra) or 
    # linha inferior
    (tabuleiro[6] == letra and tabuleiro[7] == letra and tabuleiro[8] == letra) or 
    # coluna esquerda
    (tabuleiro[0] == letra and tabuleiro[3] == letra and tabuleiro[6] == letra) or 
    # coluna do meio
    (tabuleiro[1] == letra and tabuleiro[4] == letra and tabuleiro[7] == letra) or 
    # coluna direita
    (tabuleiro[2] == letra and tabuleiro[5] == letra and tabuleiro[8] == letra) or 
    # diagonal da posição 1 até o 9
    (tabuleiro[0] == letra and tabuleiro[4] == letra and tabuleiro[8] == letra) or 
    # diagonal da posição 3 até o 7
    (tabuleiro[2] == letra and tabuleiro[4] == letra and tabuleiro[6] == letra)
    ) 


# Funcao para jogar
def jogar():
    mostraJogo(tabuleiro)
    # Definindo as letras dos jogadores
    jogador1_letra = 'X'
    jogador2_letra = 'O'

    vez_do_jogador = 1
    jogando = True
    
    while jogando:
        # Verifica de quem é a vez
        if vez_do_jogador % 2 != 0:
            mostraJogo(tabuleiro)
            print('\n\t{}Jogador 1{} é sua vez!'.format(cores['azul'], cores['limpa']))
            letra = jogador1_letra
        else:
            mostraJogo(tabuleiro)
            print('\n\t{}Jogador 2{} é sua vez!'.format(cores['amarelo'], cores['limpa']))
            letra = jogador2_letra
        
        
        escolha = input("\nEscolha uma posição (1-9): ")
        is_num = escolha.isnumeric()
        if is_num == True:
                escolha = int(escolha)
                if escolha in range(1,10):
                    # Verificando se está ocupado a posição e o jogador escolheu
                    if (tabuleiro[escolha-1] == 'X' or tabuleiro[escolha-1] == 'O'):
                        print('\t{}Já está ocupado!{}'.format(cores['vermelho'], cores['limpa']))
                        escolha = int(input("\nEscolha uma posição (1-9): ")) 
                    # Para quando o jogador jogou em uma posição livre 
                    if(tabuleiro[escolha-1] != 'X' or tabuleiro[escolha-1] != 'O'):
                        tabuleiro[escolha-1] = letra 
                        # Verificando se o jogador ganhou
                        if jogador_ganhou(letra):
                            mostraJogo(tabuleiro)
                            if letra == jogador1_letra:
                                print('\n\t{}Parabéns Jogador 1, você ganhou!{}'.format(cores['verde'], cores['limpa']))
                            else:
                                print('\n\t{}Parabéns Jogador 2, você ganhou!{}'.format(cores['verde'], cores['limpa']))
                            jogando = False

                        # Verifica se deu velha
                        elif all(isinstance(i, str) for i in tabuleiro):
                            mostraJogo(tabuleiro)
                            print('\n\t{}Deu VELHA!!!{}'.format(cores['roxo'], cores['limpa']))
                            jogando = False

                        # Se ninguém ganhou e o jogo não empatou, passa a vez para o outro jogador
                        else:
                            vez_do_jogador += 1
                else:
                    escolha_int = int(escolha)
                    while True:
                        if escolha not in range(1,10):  
                            print('{}[ERRO]{} DIGITE UMA POSIÇÃO VÁLIDA!'.format(cores['vermelho'], cores['limpa']))
                            escolha = int(input("\nEscolha uma posição (1-9): "))
                        else:
                            break

                    # Para quando o jogador jogou em uma posição livre 
                    escolha = int(escolha)
                    if(tabuleiro[escolha-1] != 'X' or tabuleiro[escolha-1] != 'O'):
                        tabuleiro[escolha-1] = letra 
                        # Verificando se o jogador ganhou
                        if jogador_ganhou(letra):
                            mostraJogo(tabuleiro)
                            if letra == jogador1_letra:
                                print('\n\t{}Parabéns Jogador 1, você ganhou!{}'.format(cores['verde'], cores['limpa']))
                            else:
                                print('\n\t{}Parabéns Jogador 2, você ganhou!{}'.format(cores['verde'], cores['limpa']))
                            jogando = False

                        # Verifica se deu velha
                        elif all(isinstance(i, str) for i in tabuleiro):
                            mostraJogo(tabuleiro)
                            print('\n\t{}Deu VELHA!!!{}'.format(cores['roxo'], cores['limpa']))
                            jogando = False

                        # Se ninguém ganhou e o jogo não empatou, passa a vez para o outro jogador
                        else:
                            vez_do_jogador += 1
        else:
            print('\t\tDigite apenas {}NÚMEROS{}!!!'.format(cores['vermelho'], cores['limpa']))
            escolha = input("\nEscolha uma posição (1-9): ")
            


jogar()