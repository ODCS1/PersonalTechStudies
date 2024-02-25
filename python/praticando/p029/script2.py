
from os import system as sy
from random import randint
from emoji import emojize

# Estabelecer valores iniciais para o jogo


# 1. Solicitrar o chute
# 2. Verificar se acertou
# 2.1 Acertou, acabou o jogo
# 2.2 Diz se esta maior ou menor
# 3 Volta ao ponto 1



# tentativas de chute

# quente ou frio
# maior ou menor



cores = {'limpa':'\033[m', 
         'vermelho':'\033[31m', 
         'verde':'\033[32m', 
         'amarelo':'\033[33m', 
         'azul':'\033[34m', 
         'roxo':'\033[35m', 
         'azulclaro':'\033[36m', 
         'cinza':'\033[37m'}
emojis = {'1°': ':1st_place_medal:',
          '2°': ':2nd_place_medal:',
          '3°': ':3rd_place_medal:',
          'lose': ':downcast_face_with_sweat:'}

res = 's'

# Estrutura para o usuário jogar outras vezes caso queira
while res == 's' or res == 'sim':
    inicial = 1
    final = 10
    tentativas = 3
    numero_Adivinhar = randint(inicial, final)
    sy('cls')
    print('\t\t', '-'*40)
    print('\t\t|{}{:^40}{}|'.format(cores['azul'], 'JOGO DO ADIVINHA', cores['limpa']))
    print('\t\t','-'*40)
    print('')
    print('\tOBJETIVO DO JOGO SERÁ {}ADIVINHAR{} O VALOR INTEIRO DE {}1{} A {}10{}.'.format(cores['vermelho'], cores['limpa'], cores['amarelo'], cores['limpa'], cores['amarelo'], cores['limpa']))


    number_User = input('\nTENTATIVAS RESTANTES[{}{}{}]: '.format(cores['azulclaro'] ,tentativas, cores['limpa']))

    is_num = number_User.isnumeric()
    
    # Verificação se o usuário colocou um dado do tipo número
    if is_num == True:
        number_User = int(number_User)

        # Verificando se o usuário escolheu apenas as opções de números disponíveis
        if number_User < 1 or number_User  > 10:
            print('\t\t\t{}Escolha uma opção válida!{}'.format(cores['amarelo'], cores['limpa'])) 
        elif number_User == numero_Adivinhar:
            print(emojize('\t{}PARABÉNS{}{} VOCÊ ACERTOU POSSUINDO {}3{} TENTATIVAS.'.format(cores['verde'], cores['limpa'], emojis['1°']*3, cores['amarelo'], cores['limpa'])))
        # Caso o usuário errar a 1° tentativa e adicionar um número válido entra no else
        else:
            tentativas -= 1

            # Informa se o valor colocado na 1° tentativa está perto do sorteado
            is_Close = abs(numero_Adivinhar - number_User)
            if is_Close == 1:
                print('\t\t\t\t{}ESTÁ TOSTANDO!{}'.format(cores['vermelho'], cores['limpa']))
            elif is_Close <= 3:
                print('\t\t\t\t{}ESTÁ MORNO!{}'.format(cores['amarelo'], cores['limpa']))
            else:
                print('\t\t\t\t{}ESTÁ FRIO!{}'.format(cores['azul'], cores['limpa']))

            # Estrutura para fazer as solicitações de valores até possuir tentativas.
            while tentativas > 0 and number_User != numero_Adivinhar:
                number_User = input('\nTENTATIVAS RESTANTES[{}{}{}]: '.format(cores['azulclaro'] ,tentativas, cores['limpa']))

                # Verificação se o usuário colocou um dado do tipo número na 2° e 3° tentativas
                is_num = number_User.isnumeric()
                if is_num == True:
                    number_User = int(number_User)

                    # Verificando se o usuário escolheu apenas as opções de números disponíveis para 2° e 3° tentativas
                    if number_User < 1 or number_User  > 10:
                        print('\t\t\t{}Escolha uma opção válida!{}'.format(cores['amarelo'], cores['limpa'])) 
                        break
                    else:                        
                        # Estrutura para quando o usuário estiver errando
                        if number_User != numero_Adivinhar:
                            is_Close = abs(numero_Adivinhar - number_User)
                            if is_Close == 1 and tentativas == 2:
                                print('\t\t\t\t{}ESTÁ TOSTANDO!{}'.format(cores['vermelho'], cores['limpa']))
                            elif is_Close <= 3 and tentativas == 2:
                                print('\t\t\t\t{}ESTÁ MORNO!{}'.format(cores['amarelo'], cores['limpa']))
                            elif is_Close > 3 and tentativas == 2:
                                print('\t\t\t\t{}ESTÁ FRIO!{}'.format(cores['azul'], cores['limpa']))
                            tentativas -= 1
                        # Caso acerte com 2 tentativas
                        elif tentativas == 2:
                            print(emojize('\t{}PARABÉNS{}{} VOCÊ ACERTOU POSSUINDO 2 TENTATIVAS.'.format(cores['verde'], cores['limpa'], emojis['2°']*3)))
                        # Caso acerte na última tentativa   
                        elif tentativas == 1:
                            print(emojize('\t{}PARABÉNS{}{} VOCÊ ACERTOU POSSUINDO 1 TENTATIVA.'.format(cores['verde'], cores['limpa'], emojis['3°']*3)))

                # Caso o usuário não digite um número na 2° ou 3° tentativa, entra no else...
                else:
                    print('\t\t\t{}[ERRO]{} DIGITE APENAS NÚMEROS!'.format(cores['vermelho'], cores['limpa']))
                    break
            # Usuário perdeu todas as tentativas
            if tentativas == 0:
                print(emojize('\t{}GAME OVER!!!{} VOCÊ ESTÁ SEM SORTE {} .'.format(cores['vermelho'], cores['limpa'], emojis['lose'])))

    # Caso o usuário não digite um número na 1° tentativa, entra no else...
    else:
        print('\t\t\t{}[ERRO]{} DIGITE APENAS NÚMEROS!'.format(cores['vermelho'], cores['limpa']))

            
    res = input('Quer jogar novamente[s/n]: ').lower()


print('\t\t\t\t{}SAINDO...{}'.format(cores['amarelo'], cores['limpa']))