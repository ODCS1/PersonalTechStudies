# Criar um vetor com 5 e tamanho, onde depois do usuário colocar os valores, o sistema msotra qual foi o menor valor digitado e qual a sua respectiva posição.

vetor = [0] * 5

i_menorValor = 0
for i in range(len(vetor)):
    vetor[i] = int(input(f'Digite o menor valor({i}): '))
    if i == 0:
      menor_valor = vetor[0]

    elif vetor[i] < menor_valor:
        menor_valor = vetor[i]
        i_menorValor = i

print(vetor)
print(f'O menor valor digitado foi {menor_valor}, na posição {i_menorValor}.')
