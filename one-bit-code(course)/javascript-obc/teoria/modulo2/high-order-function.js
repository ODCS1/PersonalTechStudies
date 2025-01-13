// HIGH ORDER FUNCTION

// É UMA FUNÇÃO QUE RECEBE UMA OUTRA FUNÇÃO COMO PARÂMETRO

function calcular (a, b, operacao) {
    console.log("Realizando Operação!")
    const resultado = operacao(a, b)
    return resultado
}

function somar (x, y) {
    return x + y
}

somando = calcular(3, 5, somar)

subtraindo = calcular(8, 4, function (x, y) {
    return x - y
})

console.log("SOMA: ", somando)
console.log("Subtraindo: ", subtraindo)

// Na prática, as funções anônimas são usadas como parâmetros para high order functions.

// EXEMPLO REAL

function exibirElemento (elemento, indice, array) {
    console.log({
        elemento,
        indice,
        array
    })
}

const lista = ["Maça", "Banana", "Laranja", "Limão"]

for (let i = 0; i < lista.length; i++) {
    exibirElemento(lista[i], i, lista)
}

lista.forEach(exibirElemento)

// CALLBACK FUNCTION = função parâmetro de uma high order function

lista.forEach(function (elemento, indice, array) {
    console.log({
        elemento,
        indice,
        array
    })
})