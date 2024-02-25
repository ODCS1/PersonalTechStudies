cont = 1

menor = float('inf')
segundoMenor = float('inf')
terceiroMenor = float('inf')
maior = float('-inf')

while cont < 5:
    num = input(f"Digite o {cont} valor: ")

    if num.isdigit() or (num[0] == '-' and num[1:].isdigit()):
        num = int(num)

        if menor > num:
            terceiroMenor = segundoMenor
            segundoMenor = menor
            menor = num
        elif segundoMenor > num:
            terceiroMenor = segundoMenor
            segundoMenor = num
        elif terceiroMenor > num:
            terceiroMenor = num

        if maior < num:
            maior = num
        
        cont += 1

    else:
        print("Digite um valor válido!")


print(f"ORDEM: {menor}, {segundoMenor}, {terceiroMenor} e {maior}")