# Ex 4 - RA: 23505

# Criação do vetor vazio
vetor = []

# Laço para preenchimento do vetor com valores inteiros
while True:
    valor = int(input("Digite um valor inteiro (ou um valor negativo para sair): "))
    if valor < 0:
        break
    vetor.append(valor)

# Exibição do vetor
print("Vetor:", vetor)

# Contagem dos valores maiores do que 5
maiores_que_5 = sum(1 for x in vetor if x > 5)
print("Quantidade de valores maiores do que 5:", maiores_que_5)

# Soma dos valores pares e ímpares
soma_pares = sum(x for x in vetor if x % 2 == 0)
soma_impares = sum(x for x in vetor if x % 2 != 0)
print("Soma dos valores pares:", soma_pares)
print("Soma dos valores ímpares:", soma_impares)

# Quantidade total de valores armazenados no vetor
quantidade = len(vetor)
print("Quantidade total de valores armazenados:", quantidade)
