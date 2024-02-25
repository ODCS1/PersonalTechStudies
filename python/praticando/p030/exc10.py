# 3 - Tabuada: Crie um programa que solicite ao usuário um número e, em seguida, exiba a tabuada desse número de 1 a 10.

def header ():
    print('-'*40)
    print("|{}{:^38}{}|".format("\033[34m", "TABUADA", "\033[m"))
    print('-'*40)

def solicitaNum ():
    while True:
        n = input("Digite um número natural exceto 0: ")

        if n.isdigit():
            n = int(n)
            if n == 0: continue

            return n
        else:
            continue

def mostraTabuada (num):
    for i in range(1, 11):
        print(f"{i} X {num} = {i*num}")

def main ():
    header()
    num = solicitaNum()
    mostraTabuada(num)

if __name__ == "__main__":
    main()