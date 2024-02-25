# Faça um programa que leia um número qualquer e mostre o seu fatorial.
# 
# Ex: 5! = 5x4x3x2x1=120

def menu():
    print("-*-" * 15)
    print("!{:^43}!".format("FATORIAL"))
    print("-*-" * 15)

def fatorial():
    menu()
    while True:
        valor = input("Digite um número para calcular o seu fatorial: ")
        if valor.isnumeric():
            valor = int(valor)
            break
        else:
            print("DIGITE VALORES VÁLIDOS!")

    mult = valor
    string = str(valor)
    menor = valor
    while True:
        menor -= 1
        if valor == 0:
           mult = 1
           break
        else:
            if menor > 0:
                mult *= menor
                string += 'x' + str(menor)
            else:
                break
    if valor > 0:
        print(f"{valor}! = {string}={mult}")
    else:
        print(f"{valor}! = {mult}")

fatorial()