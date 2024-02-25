const express = require("express")
const app = express()
const porta = 3000

app.get("/", (req,res) => {
    res.send("<h1>Bem vindo a minha página</h1><h2>Utilizando o express<h2/>")
})

app.get("/carrinho", (req,res) => {
    res.send("<h1>Aqui está o seu carrinho de compras</h1>")
})

app.get("/perfil/:nome/:idade", (req,res) => {
    res.send("<h1>Perfil</h1>" + `<h2>Nome: ${req.params.nome}</h2>` + `<h3>Idade: ${req.params.idade}</h3>`)
})

app.listen(porta, () => {
    console.log(`Servidor ON na porta ${porta}`)
})