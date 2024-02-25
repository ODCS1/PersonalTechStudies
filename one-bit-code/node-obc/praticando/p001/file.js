const fs = require('fs')

// fs.writeFile('teste.txt', 'Olá, mundo!', err => {
//     console.log("Deu erro! ---> ", err)
// })

/**
 * O write file sobreescreve todo o arquivo, caso seja uma necessidade manter o conteúdo anterior e adicionar um novo conteúdo, poderá ser  utilizado o appendFile.
 */

// fs.appendFile('teste.txt', ' -> Adicionado', err => {
//     console.log(err)
// })

// AGORA PARA RENOMEAR O ARQUIVO

// fs.rename('teste.txt', 'teste2.txt', err => {
//     console.log(err)
// })

// AGORA PARA REMOVER UM ARQUIVO

// fs.unlink('teste2.txt', err => {
//     console.log(err)
// })

console.log(__dirname)