/*  Escreva um programa em javascript que permita inserir o nome e a velocidade de dois veículos e exiba na tela uma mensagem dizendo qual dos dois é mais rápido (ou que as celocaides são iguais se este for o caso)
*/
let nome_car1 = window.prompt('Nome do 1° carro: ')
let car1 = Number(window.prompt('Velocidade do 1° carro: '))
let nome_car2 = window.prompt('Nome do 2° carro: ')
let car2 = Number(window.prompt('Velocidade do 2° carro: '))

if (car1 > car2){
  alert(`O ${nome_car1} possuí uma velocidade maior que o ${nome_car2}.`)
}else if (car1 < car2){
  alert(`O ${nome_car1} possuí uma velocidade menor que o ${nome_car2}.`)
}else{
  alert(`Os carros ${nome_car1} e ${nome_car2}, possuem a mesma velocidade.`)
}


// let name_car1 = prompt('Nome do 1°carro: ')
// let vel_car1 = Number(prompt('Velocidade do 1°carro: '))
// let name_car2 = prompt('Nome do 2° carro: ')
// let vel_car2 = Number(prompt('Velocidade do 2° carro: '))


// if (vel_car1 > vel_car2){
//   alert(`${name_car1} está mais rápido do que ${name_car2}.`)
// }else if(vel_car1 < vel_car2){
//   alert(`${name_car1} está mais devagar do que ${name_car2}`)
// }else{
//   alert(`Os carros ${name_car1} e ${name_car2}, possuem a mesma velocidade.`)
// }