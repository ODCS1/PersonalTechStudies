# 2 - Ordenação de Lista: Implemente um algoritmo de ordenação, como o Bubble Sort ou o Merge Sort, para classificar uma lista de números.

def bubbleSort(vet):
    aux = 0
    for i in range(len(vet) - 1):
        for j in range(i+1, len(vet)):
            if vet[i] > vet[j]:
                aux = vet[i]
                vet[i] = vet[j]
                vet[j] = aux
    
    return vet


vet = [4, 1, 16, 38, 34, 7]


print(bubbleSort(vet))