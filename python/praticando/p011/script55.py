nome = str(input('Nome funcionário: '))
sala = float(input('Salário atual do funcionário: '))
gen = str(input('Genêro[m/f]: '))
anose = int(input('Anos na empresa: '))
if gen == 'f':
    if anose < 15:
        sala = sala + sala*(5/100)
    elif anose > 15 and anose <= 20:
        sala = sala + sala*(12/100)
    else:
        sala = sala + sala*(23/100)
elif gen == 'm':
    if anose < 20:
        sala = sala + sala*(3/100)
    elif anose > 20 and anose <= 30:
        sala = sala + sala*(13/100)
    else:
        sala = sala + sala*(25/100)
else:
    print('Você digitou o gênero errado, por vafor coloque m para masculino e f para feminino.')

print('O novo salário de {} é R${} reais.'.format(nome,sala))
    