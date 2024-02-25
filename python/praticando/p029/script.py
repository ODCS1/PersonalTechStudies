ateOnde = int(input('Digite o valor final da sequência: '))

inicio = int(input('Digite o valor inicial: '))

if inicio > ateOnde:
  salto = 1
  while salto <= ateOnde:
      print(salto)
      salto += 1
elif inicio < ateOnde:
   salto = -1
   while salto >= ateOnde:
      print(salto)
      salto -= 1