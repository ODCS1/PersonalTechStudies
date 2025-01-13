// OBJETOS NOS JAVASCRIPT

/**
 * É uma estrutura de dados para se trabalhar
 * com dicioários chave-valor
 * 
 * O par chave-valor em um objeto javascript é
 * chamado de propriedade
 * 
 * 
 * Diferente dos arrays, seus elementos não possuem
 * nenhuma sequência
 * 
 * Uma propriedade também pode ter strings, números e booleanos como chave
 * 
 * Uma propriedade pode armazenar através de chaves {} let objeto = {}
 * 
 * Suas propriedades e funções podem ser referenciadas por encadeamento com ponto "." ou colchetes[]
 */


let obj = {}
let nome = "prop"

obj.prop = "ASDF"

console.log(obj)

obj.prop2 = "123435"
obj.prop = "ipo"

console.log(obj)
console.log(obj.prop)

console.log("obj.prop === obj['prop']: ", obj.prop === obj["prop"]) // true

let funcao = "log"

console[funcao]("obj.prop === obj[nome]: ", obj.prop === obj[nome]) // true

console["lo" + "g"]("obj.prop === obj['pro' + 'p]: ", obj.prop === obj["pro" + "p"]) // true


/**
 * Esse dinamismo está presente tanto quando está se refirindo
 * a funções dentro de objetos e quando está referenciando propriedades.
 */


let pessoa = {}

pessoa.nome = "Nome Teste"

pessoa.endereco = {
    rua: "Professor Zeferino Silva",
    bairro: "Santos Batista",
    numero: 893465,
    cidade: "Frankfurt",
    estado: "Hessen"
}

pessoa.amigos = [
    "Lucas",
    "Pedro",
    "Chico"
]

console["l" + "og"](pessoa)