/*  Escreva um programa em javascript que funcione com um conversor de medidas.
O programa deverá pedir por um valor em metros e então dar a opção de escolher para qual unidade de medida esse valor deve ser convertido. As opções são:

  - milímetro (mm)
  - centímetro (cm)
  - decímetro (dm)
  - hectômetro (hm)
  - quilômetro (km)

O programa deve então converter a medida de acordo com a opção escolhida e exibir o resultado.

O programa também deve exibir uma mensagem de "Opção inválida" caso o usuário insira uma opção diferente das disponíveis (use o break e o default para isso).

Obs: Utilizando o switch nesse
*/

let valor = Number(prompt('Digite um comprimento em metro: '))
let opcoes = prompt('As opções para tranformação: \n Para milímetro: mm \n Para centímetro: cm \n Para decímetro: dm \n Para hectômetro: hm \n Para quilômetro: km')

switch (opcoes){
  case 'mm':
    valor *= 1000
    alert(`O valor foi convertido de metro para ${opcoes}, ficando ${valor}${opcoes}.`)
    break
  case 'cm':
    valor *= 100
    alert(`O valor foi convertido de metro para ${opcoes}, ficando ${valor}${opcoes}.`)
    break
  case 'dm':
    valor *= 10
    alert(`O valor foi convertido de metro para ${opcoes}, ficando ${valor}${opcoes}.`)
    break
  case 'hm':
    valor *= 1/100
    alert(`O valor foi convertido de metro para ${opcoes}, ficando ${valor}${opcoes}.`)
    break
  case 'km':
    valor *= 1/1000
    alert(`O valor foi convertido de metro para ${opcoes}, ficando ${valor}${opcoes}.`)
    break
  default:
    alert('Opção inválida, escolha uma opção disponível para continuar.')
}



// let valor2 = Number(prompt('Digite uma distância em metros(m): '))
// let opcoes2 = prompt('OPÇÕES DE TRANSFORMAÇÃO: \nOpção 1: milímetro(mm) \nOpção 2: centímetro(cm) \nOpção 3: decímetro(dm) \nOpção 4: hectômetro(hm) \nOpção 5: quilômetro(km) \nDigite: ')

// switch (opcoes2){
//   case 'mm':
//     valor2 *= 1000
//     alert(`O valor final ficou ${valor2}${opcoes2}.`)
//     break
//   case 'cm':
//     valor2 *= 100
//     alert(`O valor final ficou ${valor2}${opcoes2}.`)
//     break
//   case 'dm':
//     valor2 *= 10
//     alert(`O valor final ficou ${valor2}${opcoes2}.`)
//     break
//   case 'hm':
//     valor2 *= 1/100
//     alert(`O valor final ficou ${valor2}${opcoes2}.`)
//     break
//   case 'km':
//     valor2 *= 1/1000
//     alert(`O valor final ficou ${valor2}${opcoes2}.`)
//     break
//   default:
//     alert('Opção Inválida...')
// }