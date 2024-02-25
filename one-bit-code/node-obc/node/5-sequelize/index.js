const express = require('express')
const app = express()
const handlebars = require('express-handlebars')
const bodyParser = require('body-parser')
const Post = require('./models/Post')

const porta = 3000

// config
    // Template Engine
        // app.engine('handlebars', handlebars.engine({defaultLayout: 'main'}))
    app.engine('handlebars',handlebars.engine({defautLayout: 'main',
        runtimeOptions: {
            allowProtoPropertiesByDefault: true,
            
            allowProtoMethodsByDefault: true,
        }}))
    app.set('view engine', 'handlebars')
    // Body Parser
    app.use(bodyParser.urlencoded({extended: false}))
    app.use(bodyParser.json())



app.get("/", (req,res) => {
    Post.findAll({order: [['id', 'desc']]}).then((posts) => {
        res.render('home', {posts: posts})
    })
})

app.get("/postagem", (req,res) => {
    res.render("formulario")
})

app.post("/add", (req,res) => {
    let novoTitulo = req.body.titulo
    let novoConteudo = req.body.conteudo
    Post.create({
        titulo: novoTitulo,
        conteudo: novoConteudo
    }).then(() => {
        // res.send("Post criado com sucesso!")
        res.redirect("/")
    }).catch( (erro) => {
        res.send("ERRO NA CRIAÇÃO DO POST!" + erro)
    })
    // res.send("<h1>Dados recebidos com sucesso!</h1>" + `<p><strong>Título:</strong> ${novoTitulo}</p>` + `<p><strong>Conteúdo:</strong> ${novoConteudo}</p>`)
})

app.get("/deletar/:id", (req,res) => {
    Post.destroy({where: {'id': req.params.id}}).then(() => {
        res.redirect("/")
    }).catch((erro) => {
        res.send("ERRO: " + erro)
    })
})


app.listen(porta, () => {
    console.log(`Servidor ON na porta ${porta}`)
})