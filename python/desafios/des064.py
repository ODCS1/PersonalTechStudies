# Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quanos números form digitados e qual foi a soma entre eles(Desconsiderando o Flag.)

print("-"*40)
print("|{:^38}|".format("VALORES"))
print("-"*40)
print("\tPara sair do programa digite 999.")

soma = 0
qtd = 0
while True:
    valor = int(input("Digite o valor: "))

    if valor != 999:
        soma += valor
        qtd += 1
    else:
        break


print(f"Quantidade de valores digitados: {qtd} \nSoma total: {soma}")