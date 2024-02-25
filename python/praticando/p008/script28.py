print('='*20)
print('| {:^18} |'.format('TRIÂNGULO'))
print('='*20)
l1 = int(input('Digite o 1° lado: '))
l2 = int(input('Digite o 2° lado: '))
l3 = int(input('Digite o 3° lado: '))

if l1 + l2 > l3 and l2 + l3 > l1 and l3 + l1 > l2:
  if l1 == l2 and l1 == l3:
      print('O triângulo em questão é do tipo equilátero.')
  elif l1 == l2 and l1 != l3:
      print('O triângulo em questão é do tipo isóceles.')
  else:
      print('O triângulo em questão é do tipo escaleno.')
else:
    print('O lados colocados não formão um triângulo.')
    
