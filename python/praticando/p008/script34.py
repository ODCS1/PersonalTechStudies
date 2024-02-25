# Receber 5 posições de um vetor e mostrar ele formatado na tela utilizando o comando for.

vetor = [0] * 5

for i in range(len(vetor)):
    vetor[i] = int(input(f'Digite um valor para posição({i}): '))


for i in range(len(vetor)):
    print(vetor[i])