let l1 = 3
let l2 = 4
let l3 = 5

if (l1 == l2 && l1 == l3){
    let r1 = console.log('Triângulo equilátero')
} else if(l1 == l2 && l1 != l3){
    let r2 = console.log('Triãngulo isóceles')
} else if(l1 != l2 && l2 != l3 && l1 != l3){
    let r3 = console.log('Triângulo escaleno')
}

if (r1 == true){
    console.log('O triângulo equilátero é um triângulo especial, onde todos os seu lados são congruentes assim como os seus ângulos também são congruentes.')
} else if(r2 == true){
    console.log('O triângulo isóceles possuí 2 lados congruentes, assim como esses 2 lados tem ângulos congruentes também.')
    } else if(r3 == true){
        console.log('O triângulo escaleno possuí todos os lados diferentes, onde todos os seus ângulos consequentemente são também diferentes.')
    }