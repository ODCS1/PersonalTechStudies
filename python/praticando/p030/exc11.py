# 4 - Verificação de Ano Bissexto: Escreva um programa que verifique se um ano fornecido pelo usuário é bissexto ou não. Um ano bissexto é aquele que é divisível por 4, a menos que também seja divisível por 100. No entanto, se for divisível por 400, ele é bissexto.

def veficaAnoBissexto (num):
    if num % 400 == 0:
        return True
    else:
        return False

def entradaValor ():
    while True:
        n = input("Digite um ano: ")

        if n.isdigit():
            return int(n)
        else:
            continue


def main ():
    num = entradaValor()
    anoBissexto = veficaAnoBissexto(num)

    if anoBissexto:
        print(f"{num} é ano bissexto.")
    else:
        print(f"{num} não é ano bissexto.")


if __name__ == "__main__":
    main()