# Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

res = "s"
soma = 0
menorValor = 100
maiorValor = 0
print("Intervalo entre [0, 100]")
while res in ["s", "sim"]:
    valor = int(input("Digite o valor: "))
    if 101 > valor >= 0:
        soma += valor
        if menorValor > valor:
            menorValor = valor

        if maiorValor < valor:
            maiorValor = valor

        res = input("Quer continuar [s/n]: ")
    else:
        print("Digite um valor válido.")

print(f"Soma: {soma} \nMenor valor: {menorValor} \nMaior Valor: {maiorValor}")