var agora = new Date()
var diaSem = agora.getDay()

/*
    0 - Domingo
    1 - Segunda
    2 - Terça
    3 - Quarta
    4 - Quinta
    5 - Sexta
    6 - Sábado
*/

console.log(diaSem)

switch (diaSem){
  case 0:
    console.log('Domingo')
    break
  case 1:
    console.log('Segunda')
    break
  case 2:
    console.log('Terça')
    break
  case 3:
    console.log('Quarta')
    break
  case 4:
    console.log('Quinta')
    break
  case 5:
    console.log('Sexta')
    break
  case 6:
    console.log('Sábado')
    break
  default:
    console.log('[ERRO] Dia inválido!')
    break
}

// Treinando mais uma vez
// var agora = new Date()
// var diaSem = agora.getDate()

// switch (diaSem){
//   case 0:
//     console.log('Domingo')
//     break
//   case 1:
//     console.log('Segunda')
//     break
//   case 2:
//     console.log('Terça')
//     break
//   case 3:
//     console.log('Quarta')
//     break
//   case 4:
//     console.log('Quinta')
//     break
//   case 5:
//     console.log('Sexta')
//     break
//   case 6:
//     console.log('Sábado')
//     break
//   default:
//     console.log('[ERRO] Dia inválido')
//     break
// }

// Praticando

// var agora = new Date()
// var horas = agora.getHours()

// if (horas >= 5 && horas < 12){
//   console.log('Bom dia!')
// } else if (horas >= 12 && horas < 18){
//   console.log('Boa Tarde!')
// } else if (horas >= 18 && horas < 24){
//   console.log('Boa noite!')
// } else{
//   console.log('Boa madrugada!')
// }