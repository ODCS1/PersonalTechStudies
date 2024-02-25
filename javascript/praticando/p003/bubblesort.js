// Ordenando vetor pelo bubble sort

function bubbleSort(vetor) {
    const n = vetor.length

    for (let i = 0; i < n - 1; i++) {
        for (let j = i + 1; j < n; j++) {
            if (vetor[i] > vetor[j]) {
                let aux = vetor[i]
                vetor[i] = vetor[j]
                vetor[j] = aux
            }
        }
    }

    return vetor
}


let vetorAleatorio = [56,34,2,76,432,2]
let vetorOrganizado = bubbleSort(vetorAleatorio)

console.log(`O vetor organizado ficou: ${vetorOrganizado}.`)
