# Crie um programa que faça o computador jogar Jokempô com você.

from random import choice
from os import system as sy
from emoji import emojize as e

lista = ['pedra', 'papel', 'tesoura']

cores = {'limpa':'\033[m', 
         'vermelho':'\033[31m', 
         'verde':'\033[32m', 
         'amarelo':'\033[33m', 
         'azul':'\033[34m', 
         'roxo':'\033[35m', 
         'azulclaro':'\033[36m', 
         'cinza':'\033[37m'}

emojis = {'1°': ':1st_place_medal:',
          'lose': ':downcast_face_with_sweat:',
          'pedra': ':moai:',
          'papel': ':newspaper:',
          'tesoura': ':scissors:'}

# Repetição para continuar jogando
res = 's'
while res == 's':
  sy('cls')
  print('\t\t', '-' * 40)
  print('\t\t|{}{:^38}{}|'.format(cores['azul'], 'JOKENPÔ', cores['limpa']))
  print('\t\t' ,'-' * 40)
  print('')

  bot = choice(lista)
  human = input(e('\tPedra{} [1], Papel{} [2] ou Tesoura{} [3]? \nDigite: '.format(emojis['pedra'], emojis['papel'], emojis['tesoura'])))
  is_Num = human.isnumeric()

  if is_Num == True:
    human = int(human)
    if human < 1 or human > 3:
      print(f'{cores["amarelo"]}Escolha uma opção válida!{cores["limpa"]}')
    else:
      if is_Num == True:
        human = int(human)
        if human < 1 or human > 3:
          print(f'{cores["amarelo"]}Escolha uma opção válida!{cores["limpa"]}')
        else:
          if bot == 'pedra' and human == 2 or bot == 'papel' and human == 3 or bot == 'tesoura' and human == 1:
              print(e(f'Você: {human} \nComputador: {bot}'))
              print(e(f'\t\t\t{cores["verde"]}Você ganhou!!!{cores["limpa"]} {emojis["1°"] * 3}'))
          elif bot == 'pedra' and human == 1 or bot == 'papel' and human == 2 or bot == 'tesoura' and human == 3:
             print(f'{cores["azul"]}Você:{cores["limpa"]} {human} \n{cores["azul"]}Computador:{cores["limpa"]} {bot}')
             print(f'\t\t\t{cores["azulclaro"]}Empate!{cores["limpa"]}')
          else:
              print(f'Você: {human} \nComputador: {bot}')
              print(e(f'\t\t\t{cores["vermelho"]}Você perdeu!!!{cores["limpa"]} {emojis["lose"] * 3}'))
    res = input('Quer jogar novamente[s/n]: ')
  else:
     print(f'{cores["vermelho"]}[ERRO]{cores["limpa"]} DIGITE APENAS NÚMEROS.')
     res = input('Quer jogar novamente[s/n]: ')

print(f'{cores["amarelo"]}Saindo...{cores["limpa"]}')