/**
 * Função na programação é um bloco de código que é colocado lá dentro
 * tudo aquilo que servirá para resolver determido problema.
 * 
 * Assim quando você precisar resolver determinado problema, será só fazer a chamada da respectiva função que é responsável por resolver o problema.
 * 
 * Dessa forma, para um problema recorrente no código, não será
 * necessário ter que fazer o mesmo código várias vezes.
 * 
 * 
 * Observe que função é diferente de módulo em 1 aspecto, que a função obrigatoriamente retorna um valor.
 */

// A PASSAGEM DE PARÂMETROS EM UMA FUNÇÃO É OPCIONAL.

// SINTAXE:

function nomeDaFuncao () {
    // CÓDIGO
    return saida
}


// EXEMPLO

function ola () {
    return "Olá"
}

console.log(ola())
console.log(ola())
console.log(ola())

// PARÂMETROS DE UMA FUNÇÃO

function dobro (x) {
    return x*2
}

let nDobro = dobro(5)
console.log(nDobro)


// EXEMPLO AGORA COM OBJETO

function criarUsuario(nome='SemNome', email='SemEmail', senha='1111', tipo='User') {
    const usuario = {
        nome: nome,
        email: email,
        senha: senha,
        tipo: tipo
    }

    return usuario
}
// NESSE CASO PODERIA FAZER ASSIM:::

// function criarUsuario(nome='SemNome', email='SemEmail', senha='1111', tipo='User') {
//     const usuario = {
//         nome,
//         email,
//         senha,
//         tipo
//     }

//     return usuario
// }


let usuario = criarUsuario("João", "meuemail@gmail.com", "asenha123")

console.log(usuario)



// AGORA UM EXEMPLO COM MUITOS PARÂMETROS:::

function muitosParametros(nome, telefone, endereco, aniversário, email, senha) {
    // ...
}

muitosParametros("nome", "351321547", "endereço", "20/06", "oemail123@gmail.com", "senha123")

// OBSERVE QUE NESSE CASO, SÃO VÁRIOS PARÂMETROS, E AINDA SÃO POUCOS QUANDO SE FALA DE GRANDES PROJETOS.

// PARA SIMPLIFICAR, PODERÁ SER CRIADO UM OBJETO PARA PASSAR ELE COMO PARÂMETRO, ASSIM JÁ COM TODOS OS VALORES RESPECTIVAMENTE.



// RETORNO DE UMA FUNÇÃO


function calcularMedia (a, b) {
    const media = (a + b) / 2
    return media
}

const resultado = calcularMedia(7, 2)

console.log(resultado)


function criarProduto(nome, preco) {
    const produto = {
        nome,
        preco,
        estoque: 1
    }
    return produto
}


const notebook = criarProduto("Notebook Intel Core i3 8GB", 2500)

console.log(notebook)


function areaRetangular(base, altura) {
    return base * altura
}

function areaQuadrada(lado) {
    return areaRetangular(lado, lado)
}

console.log(areaRetangular(3, 5))
console.log(areaQuadrada(9))


// OBSERVAÇÃO

/**
 * Observe que quando é colocado o return
 * tudo que estará abaixo, não será executado
 * pois qaundo há o return, que é o retorno da
 * função, o código da função para de ser executado
 */

function saudacao (word) {
    return word

    word = "NADA"
    console.log(word)
}

saudacao("Olá Mundo!")


// OUTRO EXEMPLO COM CONDICIONAL

function maioridade (idade) {
    if (idade < 18) {
        return false
    } else {
        return true
    }
}
