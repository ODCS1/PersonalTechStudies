# EXERCÍCIO 5

divi = 0
n_divi = 0
n = 1
while n != 0:
    n = int(input('Digite um número: '))
    for dem in range(1, n+1):
        if n % dem == 0:
            divi += 1
    if divi == 5:
      n_divi += 1

print(f'{n_divi} é o número de elementos que possuem 5 divisores.')