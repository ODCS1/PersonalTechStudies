const process = require('process')

// console.log(process.argv)

// process.stdout.write('Olá, Mundo!')

process.stdout.write("Digite o seu nome: ")

process.stdin.on('data', (keyboard) => {
    process.stdout.write(`Texto do usuário: ${keyboard}`)
    process.exit()
})

/**
 * ENTRADA E SAÍDA DE DADOS
 * UTILIZANDO O process.
 * 
 * process.stdout é um objeto, write é um método.
 *
 * process.stdin é um objeto, on é um método.
 * data significa que a entrada será de dados, logo em seguida
 * temos uma função com (keyboard) sendo um argumento passado
 * como parâmetro. O motivo dele estar dentro do process.stdin.on é que ele
 * receberá o valor que o usuário passar.
 */