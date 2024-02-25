function soma(n1, n2){
  return (n1 + n2)
}

console.log(soma(1, 3))

// Erro comum caso não seja passado a qt de parâmetros necessários na function.

function soma2(n1, n2){
  return (n1 + n2)
}
// number + undefined = NaN
console.log(soma2(8))


// Parâmetros opcionais

function soma3(n1=0, n2=0){
  return (n1 + n2)
}

console.log(soma3(9))