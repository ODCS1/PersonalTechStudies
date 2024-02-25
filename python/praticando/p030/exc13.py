# 6 - Jogo da Adivinhação: Implemente um jogo simples em que o programa gera um número aleatório entre 1 e 100, e o jogador deve adivinhar qual é esse número. O programa deve fornecer dicas (maior ou menor) após cada tentativa até que o jogador acerte.

from os import system as sy
from random import randint

def inicio ():
    sy('cls')
    print('-'*40)
    print("|{}{:^38}{}|".format("\033[34m", "ADIVINHA", "\033[m"))
    print('-'*40)
    print("\t\t1 A 100")

def geraAleatorio ():
    inicio = 1
    final = 100
    return randint(inicio, final)

def verificaNum():
    while True:
        num = input("Digite o número: ")

        if num.isdigit():
            num = int(num)
            if num >= 1 and num <= 100:
                return num
            else:
                print("Digite um número no intervalo válido!")
        else:
            print("Digite um número inteiro!!!")


def ganhou (rodadas):
    print(f"Parabéns, você ganhou em {rodadas} rodadas!")

def estaPerto (numAle, numUser):
    if numUser < numAle:
        print("NÚMERO DEVE SER MAIOR!")
    else:
        print("NÚMERO DEVE SER MENOR!")

def main ():
    inicio()

    numAlea = geraAleatorio()
    numUser = verificaNum()
    rodadas = 1

    while True:
        if numAlea == numUser:
            ganhou(rodadas)
            break
        else:
            estaPerto(numAlea, numUser)
            numUser = verificaNum()
            rodadas += 1
    
    print("\t\t{}SAINDO...{}".format("\033[36m", "\033[m"))


if __name__ == "__main__":
    main()