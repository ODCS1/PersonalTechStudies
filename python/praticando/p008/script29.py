def mostrarMenu():
    print('-'*40)
    print('|{}{:^38}{}|'.format('\033[35m', 'OPÇÕES', '\033[m'))
    print('-'*40)

def testeLógico():
  res = 1
  while res != 0:
    mostrarMenu()
    res = int(input('Resposta: '))
    return res

ver = input('Digite se quer ver[s/n]: ')

if ver == 's': resg = testeLógico()

print(resg)