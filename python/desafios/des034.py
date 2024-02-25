# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# 
# Para salários superiores a R$1.250,00, calcule um aumento de 10%.
# 
# Para os inferiores ou iguais o aumento é de 15%.

salario = float(input('Digite o salário: '))

if salario > 1250:
    nv_Salario = salario + salario * (10/100)
else:
    nv_Salario = salario + salario * (15/100)

print(f'O novo salário será de R${nv_Salario} reais.')