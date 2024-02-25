# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantos ainda não atingiram a maioridade e quantos já são maiores.

idades = []

for i in range(1, 8):
    iAtual = int(input(f'Ano de nascimento da {i}° pessoa: '))
    idades.append(iAtual)

mai_idade = 0
men_idade = 0

for i in idades:
    if idades[i] > 2004:
        mai_idade += 1
    else:
        men_idade += 1

print(f'Quantidade de pessoas que já atingiram a maioridade: {mai_idade} \nQuantidade de pessoas que não atingiram a maioridade: {men_idade}')
