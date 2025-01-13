const arr = ['Frodo', 'Sam', 'Merry', 'Pippin', 'Gandashi']

console.log(arr)

// Adicionar Elementos PUSH

arr.push('Boramir')
console.log(arr)

// Adicionar no início unshift

arr.unshift('Boramir')
console.log(arr)

// Remover elementos POP

arr.pop()

// Remove no início SHIFT

arr.shift()

// Pesquisar por um elemento retorna (true or false)
// includes

arr.includes('Frodo')

// indexof > devolve o índice do item pesquisado.

arr.indexOf('Gandashi')


// Cortar e Concatenar
// slice

arr.slice(0, 4)
// arr.slice(-3, 0)

// Concatenar -> concat
const arr2 = ['1', '2', '3']
arr.concat(arr2)


//Substituição dos Elementos
const a = ['Janeiro', 'Fevereiro', 'Março']
a.splice(0, 1, 'Primeiro')
/*  Resultado esperado:
    ['Primeiro', 'Fevereiro', 'Março']
*/

// Iterar sobre os elementos

for (let i = 0; i < a.length; i++) {
    const elemento = a[i]
    console.log(elemento)
}


for (let j in a) {
    console.log(a[j])
}

for (let z of a) {
    console.log(z)
}