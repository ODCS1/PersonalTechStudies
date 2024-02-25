function bubbleSort (vet2) {
    let n = vet2.length

    for (let i = 0; i < n - 1; i++)  {
        for (let j = i + 1; j < n; j++) {
            if (vet2[i] > vet2[j]) {
                aux = vet2[i]
                vet2[i] = vet2[j]
                vet2[j] = aux
            }
        }
    }
    return  `Vetor ordenado: ${vet2}`
}

let vet = [3, 5, 8, 2, 1, 10]

console.log(bubbleSort(vet))