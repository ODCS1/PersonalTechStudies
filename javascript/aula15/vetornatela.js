let valores = [8, 1, 7, 4, 2, 9]

console.log(valores)

// Forma tradicional

// for (let c = 0; c < valores.length; c++){
//   console.log(`O vetor na posição ${c} tem o valor ${valores[c]}`)
// }


// Forma moderna

for (let c in valores){
  console.log(`O vetor na posição ${c} tem o valor ${valores[c]}`)
}