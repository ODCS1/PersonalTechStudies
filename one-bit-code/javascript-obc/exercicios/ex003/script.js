/* Escreva um programa em javascript que permita inserir dois avlores numéricos e então calcule o resultado das quatro operações básicas (soma, subtração, multiplicação e divisão).

  Após calcular os resultados o programa deve exibi-los na tela.

*/

// const num1 = Number(prompt('Digite o 1º número: '))
// const num2 = Number(prompt('Digiteo 2º número: '))

// const som = num1 + num2
// const sub = num1 - num2
// const mult = num1 * num2
// const divi = num1 / num2

// alert(`
//        1° Número:: ${num1}\n
//        2° Número: ${num2}\n
//        Soma: ${som}\n
//        Subtração: ${sub}\n
//        Multiplicação: ${mult}\n
//        Divisão: ${divi}
// `)

const n1 = Number(prompt('Digite um número: '))
const n2 = Number(prompt('Digite outo número: '))

const soma = n1 + n2
const subtracao = n1 - n2
const multiplicacao = n1 * n2
const divisao = n1 / n2
alert(`Resultados:\n\nSoma: ${soma}\nSubtração: ${subtracao}\nMultiplicação: ${multiplicacao}\nDivisão: ${divisao}`)