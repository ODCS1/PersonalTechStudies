# PROGRAMA PARA CONTAGEM DE LETRAS EM UMA STRING


# FORMA COM BAIXA PERFOMACE

# CONTAGEM DE LETRAS
def contagem(vet, t):
    cont = 0
    for i in range(len(vet)):
        for j in range(len(t)):
            if vet[i] == t[j]:
                cont += 1

    return cont



txt = input("DIGITE O QUE QUISER: ")
txtc = txt.lower()


alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

nLetras = contagem(alfabeto, txtc)


print(f"O número de letras é {nLetras}.")


# FORMA COM PERFORMACE

# def contador(alf, txt):
#     c = 0
#     txtSize = len(txt)
#     for i in range(len(alf)):
#         if i < txtSize - 1:
#             if alf[i] == txt[i]:
#                 c += 1
#                 pass
#         else:
#             break

#     return c


# txt = "TesT hg 5TDJ dg"
# txtLow = txt.lower()

# alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# n = contador(alfabeto, txt)

# print(f"Número de letras no texto: {n}.")