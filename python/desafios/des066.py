# Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a sima entre eles (desconsiderando o flag).

qtd = 0
soma = 0
while True:
    valor = int(input("Digite o valor: "))

    if valor != 999:
        soma += valor
        qtd += 1
    else:
        print("Saindo...")
        break

print(f"Soma: {soma} \nQuantidade de números digitados: {qtd}")