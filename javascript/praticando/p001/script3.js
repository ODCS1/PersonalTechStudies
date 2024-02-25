// SELECTION SORT

function SelectionSort (vet) {
    const n = vet.length
    
    let aux = 0
    for (let j = 0; j < n; j++) {
        let menor = vet[j]
        if (vet[j] < menor) {
            menor = vet[j]
        }

        // aux = vet[j]
        // vet[j] = menor
        // vet[i] = aux
        

    }

    return vet
}

let vetor = [4, 7, 3, 9, 10, 45]

SelectionSort(vetor)
console.log(vetor)
