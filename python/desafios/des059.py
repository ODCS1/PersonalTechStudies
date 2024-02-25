# Crie um programa que leia dois valores e mostre um menu na tela:
# 
# [1] somar
# [2] multiplicar
# [3] maior
# [4] novos números
# [5] sair do programa
# 
# Seu programa deverá realizar a operação solicitada em cada caso.

def calcular(vet, escolha):
    match escolha:
        case 1:
            print("Soma dos valores: ", sum(vet))
        case 2:
            multi = 1
            for i, j in enumerate(vet): 
                multi *= j
            print("Multiplicação: ", multi) 
        case 3:
            for i, j in enumerate(vet):
                if i == 0:
                    maior = vet[i]
                else:
                    if maior < j:
                        maior = j
            print("O maior valor é: ", maior)


def menu():
    print("[1] somar \n[2] multiplicar \n[3] maior \n[4] novos números \n[5] sair do programa")
    

def rodando():
    vet = []
    n1 = int(input("Digite um número: "))
    n2 = int(input("Digite outro valor: "))
    vet.append(n1)
    vet.append(n2)
    
    while True:
        menu()
        escolha = input("Digite: ")
        if escolha.isnumeric():
            escolha = int(escolha)
            if 4 > escolha > 0:
                calcular(vet, escolha)
            elif escolha == 4:
                num = int(input("Digite o valor: "))
                vet.append(num)
            elif escolha == 5:
                print("SAINDO...")
                break
        else:
            print("\n\tEscolha valores válidos!")


rodando()