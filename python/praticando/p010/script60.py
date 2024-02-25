# SOLICITE 4 NÚMEROS INTEIROS E FAÇA UMA SAÍDA DE DADOS EM ORDEM CRESCENTE.


cont = 1

menor = float('inf')
segundoMenor = float('inf')
TerceiroMenor = float('inf')
maior = float('-inf')

while cont < 5:
    num = input(f"Digite o {cont} inteiro: ")

    if num.isdigit() or (num[0] == '-' and num[1:].isdigit()): 
        num = int(num)

        if num < menor:
            TerceiroMenor = segundoMenor
            segundoMenor = menor
            menor = num
        elif num < segundoMenor:
            TerceiroMenor = segundoMenor
            segundoMenor = num
        elif num < TerceiroMenor:
            TerceiroMenor = num

        if maior < num:
            maior = num

        cont += 1
    else:
        print("Digite um número válido!")


print(f"Valores digitados: {menor}, {segundoMenor}, {TerceiroMenor} e {maior}.")