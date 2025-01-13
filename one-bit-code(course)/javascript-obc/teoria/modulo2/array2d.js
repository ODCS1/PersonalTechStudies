/**
 * Array 2d ou array bidimensional
 * é um array que quarda basicamente outros
 * arrays, dessa forma sendo bidimensional.
 */


const matriz = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

console.log(matriz[0][0])


matriz[0].push("Adicionei")
console.log(matriz)


for (let i = 0; i < matriz.length; i++) {
    for (let j = 0; j < matriz[i].length; j++) {
        console.log(j)
    }
}