# Nome: Antonio Ilton - RA: 23505
# Exercício 1 - parte 2

nome = input('Digite algo alfabético: ')

def palindromo(nome):
    nome_invertido = ''
    for i in nome:
      nome_invertido += nome[i]
    if nome == nome_invertido:
       return (print('A palavra {} é um palíndromo, pois escrita de trás para frente fica {}'.format(nome, nome_invertido)))



