# Faça um programa que leia um nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
# 
# Ex: Ana Maria de Souza
# primeiro=Ana
# último=Souza

nome = str(input('Nome completo: '))
separado = nome.split()
print('primeiro: {} \núltimo: {}'.format(separado[0], separado[len(separado) - 1]))