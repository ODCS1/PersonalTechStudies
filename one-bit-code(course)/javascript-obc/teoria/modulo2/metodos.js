// MÉTODOS SÃO FUNÇÕES ATRELADAS A OBJETOS

let pessoa = {
    nome: "Isaac",
    idade: 26,

    // MÉTODO
    dizerOla () {
        console.log("Olá, mundo!")
    },

    dizerNome () {
        console.log(`O nome é ${this.nome}!`)
    }
}

console.log(pessoa)

pessoa.dizerOla()
pessoa.dizerNome()