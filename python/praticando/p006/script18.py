# Tuplas

lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')

for cont in range(0, len(lanche)):
    print(lanche[cont])

for comida in lanche:
    print(comida)

# Para além de mostrar o dado contido em determinada posição, for necessário que também informe a posição, poderá ser feito assim:

for pos, comida in enumerate(lanche):
    print(f'{comida} na posição {pos}')

# Ou da outra forma:

for cont in range(0, len(lanche)):
    print(f'{lanche[cont]} na posição {cont}')


# sorted ordena a tupla

# print(sorted(lanche))