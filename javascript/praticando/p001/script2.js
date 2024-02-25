function maiorValor (vetor) {
    const n = vetor.length
    let maior = vetor[0]
    for (let i = 1; i < n; i++) {
        if (vetor[i] > maior) {
            maior = vetor[i]
        }
    }
    return maior
}

const vet = [4, 10, 5, 2, 12, 47]

console.log(`Maior elemnto: ${maiorValor(vet)}`)