// ESCOPO

let pokemon = 'Charmander'
let pokemon2 = "Charizard"
function evoluir() {
    pokemon = "g"

    
}

console.log(pokemon2)

function avaliarNota(nota) {
    let situacao
    let aprovado
    if (nota > 60) {
        aprovado = true
        situacao = "Aprovado"
    }else {
        aprovado = false
        situacao = "Reprovado"
    }

    console.log(nota)
    console.log(aprovado)
    console.log(situacao)
    // ERRO POIS SITUACAO NÃO PODE SER ACESSADA
}

avaliarNota(83)
avaliarNota(49)