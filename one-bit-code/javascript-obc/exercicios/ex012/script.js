/*  Escreva um programa em javascript que seja capaz de identificar se uma palavra é um palíndromo. Um palíndromo é uma palavra que lida de trás para frente possui as mesmas letras na mesma ordem. O programa deve iniciar pedindo que seja informada uma palavra e então deve exibir uma mensagem dizendo se aquela palavra é ou não um palíndromo. Caso não seja um palíndromo, o programa deve mostrar a palavra lida da esquerda para direita e da direita para esquerda.
*/


function verificar (word) {
  let iword = ''

  for (let i = word.length - 1; i > -1; i--) {
    iword += word[i]
  }

  if (word == iword) {
    return "A palavra inserida é um palíndromo!"
  } else {
      return "A palavra inserida não é um palíndromo!"
  }
}


const palavra = prompt("Digite uma palavra para verificação: ")
alert(verificar(palavra))


// const word = prompt('Informe uma palavra: ')
// let inverted_Word = ''

// for (let i = word.length - 1; i >= 0; i--){
//   inverted_Word += word[i]
// }

// if (word == inverted_Word){
//   alert(`A palavra ${word} é um palíndromo...`)
// } else{
//   alert(`A palavra ${word} não é um palíndromo, pois o seu inverso é ${inverted_Word}.`)
// }