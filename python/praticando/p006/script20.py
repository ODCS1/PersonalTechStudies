# Nome: Antonio Ilton - RA: 23505
# Exercício 2

frase = str(input('Digite uma frase: ')).lower()
letra = str(input('Agora digite uma letra: ')).lower()

cont_letra = 0
for c in range(len(frase)):
    if frase[c] == letra:
        cont_letra += 1

print('A sua frase possuí {} letras {}.'.format(cont_letra, letra))