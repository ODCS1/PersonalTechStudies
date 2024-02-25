# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a digitação novamente até ter um valor correto.

while True:
    s: str = input("Digite: ")

    if (s in ["M", "F"]):
        print("SAINDO...")
        break
    else:
        print("Tente novamente.")