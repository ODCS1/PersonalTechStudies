# Nome: Antonio Ilton - RA: 23505
# Exercício 3

frase = str(input('Digite uma frase: '))
frase_separada = frase.split()
frase_invertida = ''

for c in frase:
    frase_invertida += c
print(frase_invertida)