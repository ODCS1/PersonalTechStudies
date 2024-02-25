# Nome: Antonio Ilton - RA: 23505
# Exercício 1

frase = str(input('Digite uma frase: ')).lower()

cont_a = 0
for n in range(len(frase)):
    if frase[n] == 'a':
        cont_a += 1

print('Na sua frase possuí {} letras a.'.format(cont_a))