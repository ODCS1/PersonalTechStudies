/* Escreva um programa em javascript que permita salvar informações de um recruta. As informações a serem salvas são:

- O primeiro nome
- O sobrenome
- O campo de Estudo
- O ano de nascimento

  Depois mostrar o nome completo do recruta, seu campo de estudo e a sua idade (apenas baseada no ano de nascimento).
*/

let nome = String(prompt('Primeiro nome: '))
let sobrenome = prompt('Sobrenome: ')
let campo_Estudo = prompt('Campo de Estudo: ')
let anasc = Number(prompt('Digite o seu ano de nascimento: '))

let aatual = new Date().getFullYear()

idade = aatual - anasc

window.alert(`O se nome completo é ${nome} ${sobrenome}, seu campo de estudo ${campo_Estudo} \nIdade: ${idade}`)