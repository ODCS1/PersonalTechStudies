# 2 - Média de Notas: Escreva um programa que recebe as notas de um aluno e calcula sua média. O programa deve permitir que o usuário insira um número indefinido de notas (até que ele decida parar) e, em seguida, calcular e exibir a média.

def calcularMedia(notas, cont):
    return notas / cont

def adicionarNotas():
    cont = 1
    notas = 0
    while True:
        n = int(input(f"Digite a {cont}° nota: "))
        if n == 0:
            break
        notas += n
        cont += 1
    cont -= 1

    return notas, cont
    

def formatar():
    print('-'*40)
    print("|{}{:^38}{}|".format("\033[34m", "MÉDIA DE NOTAS", "\033[m"))
    print('-'*40)
    print("\tPara sair digite 0!")

def main():
    formatar()
    notas, cont = adicionarNotas()
    media = calcularMedia(notas, cont)

    print(f"A média foi {media}.")


if __name__ == "__main__":
    main()