# Nome: Antonio Ilton - RA: 23505
# Exercício 4

frase = input('Digite uma frase: ')

for c in frase:
    frase = frase.replace(' ', '')
print(f'A sua frase sem espaços ficou {frase}.')