# Criar um vetor com 5 e tamanho, onde depois do usuário colocar os valores, o sistema msotra qual foi o maior valor digitado e qual a sua respectiva posição.

vetor = [0] * 5

mvalor = 0
i_maiorValor = 0
for i in range(len(vetor)):
    vetor[i] = int(input(f'Digite um valor para posição ({i}): '))
    if vetor[i] > mvalor:
        mvalor = vetor[i]
        i_maiorValor = i
  
print(vetor)
print(f'O maior valor dentro do vetor é {mvalor}, na posição {i_maiorValor}.')