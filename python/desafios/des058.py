# Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

from os import system as sy
from random import randint

def header():
    sy("cls")
    print('-'*40)
    print("|{}{:^38}{}|".format('\033[34m', '🎰ADVINHA🎲', '\033[m'))
    print('-'*40)
    print("\tEscolha entre {}0{} e {}100{}.".format('', '', '', ''))

def verificar(palpite, num_bot):
    if palpite < num_bot:
        print("O número é maior!")
    elif palpite > num_bot:
        print("O número é menor!")

def ganhou():
    print("Parabéns! Você acertou o número!")

def perdeu(num_bot):
    print(f"Que pena! O número correto era {num_bot}.")

def jogar():
    num_bot = randint(1, 100)
    header()
    
    while True:
        try:
            palpite = int(input("Digite seu palpite: "))
        except ValueError:
            print("Por favor, digite um número válido.")
            continue

        verificar(palpite, num_bot)

        if palpite == num_bot:
            ganhou()
            break

    else:
        perdeu(num_bot)

jogar()

