# 9. Escreva um programa em Python que exiba na tela a posição mais a direita de um dado 
# número em um lista de números

from os import system as sy

lista = [145, 542, 76, 38, 31]

def menu():
    sy('cls')
    print("-" * 40)
    print("|{:^38}|". format("Exercício 8"))
    print("-" * 40)
    print("Escolha um valor de posição pra uma X lista")

    print("\t[0]  -  [1]  -  [2]  -  [3]  -  [4]\n")

def validarOp(op):
    if op.isnumeric():
        op = int(op)
        if op > -1 and op < 5:
            return True
    
    return False


def solicitarOp():
    op = 0
    while True:
        op = input("Digite a opção: ")
        if validarOp(op):
            op = int(op)
            return op
        
        print("{}[ERRO]{} Digite uma opção válida!".format("\033[31m", "\033[m"))
        
def mostrarResultado(op):
    valor = str(lista[op])[-1]
    print()
    print(f"LISTA: {lista}")
    print(f"Valor mais a direita para o elemento {lista[op]} na posição {op}: {valor}")
    print()


def main():

    res = "sim"

    while res == "sim" or res == "s":
        menu()
        op = solicitarOp()
        mostrarResultado(op)

        res = input("Quer testar outro[s/n]: ").lower()

    print("\t\t{}Saindo...{}".format("\033[33m", "\033[m"))
    



if __name__ == "__main__":
    main()