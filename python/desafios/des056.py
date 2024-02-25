# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
# 
# > A média de idade do grupo
# > Qual é o nome do homem mais velho
# > Quantas mulheres têm menos de 20 anos.

def ler():
    nomes = []
    idades = []
    sx = []

    for i in range(1, 5):
        # Lendo
        nome_atual = input(f'{i}° nome: ')
        nomes.append(nome_atual)
        idade_atual = int(input(f'{i}° idade: '))
        idades.append(idade_atual)
        sx_atual = input(f'{i} Digite[h/m]: ')
        sx.append(sx_atual)

    analisar(nomes, idades, sx)

def analisar(nomes, idades, sx):
    som_idade = 0
    h_m_i = 0
    nm_h_m_v = ''
    qt_m20 = 0
    print(idades)
    for i, j in enumerate(idades):
        print(f'i: {i} j: {j}')
        som_idade += idades[i]
        # Pegar nome do homem com maior idade
        if sx[i] == 'h' and h_m_i < idades[i]:
            nm_h_m_v = nomes[i]

        if sx[i] == 'm' and idades[i] < 20:
            qt_m20 += 1

        media_idade = som_idade / len(nomes)

    mostrar(media_idade, nm_h_m_v, qt_m20)

def mostrar(media_idade, nm_h_m_v, qt_m20):
    print(f'Media de idade: {media_idade} \nNome do homem mais velho: {nm_h_m_v} \nQuantidades de mulheres com menos de 20 anos: {qt_m20}')


ler()