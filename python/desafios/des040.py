# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
# 
# - Média abaixo de 5.0: REPROVADO
# - Média entre 5.0 e 6.9: RECUPERAÇÃO
# - Média 7.0 ou superior: APROVADO

n1 = float(input('1° nota: '))
n2 = float(input('2° nota: '))

m = (n1 + n2) / 2

if m < 5:
    print('Reprovado...')
elif m <6.9:
    print('Recuperação...')
else:
    print('Aprovado! Parabéns...')