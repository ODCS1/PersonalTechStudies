const express = require('express');
const porta = 3000;


// Chamada do express para ter acesso a todos os métodos referentes ao nosso servidor, disponível dentro de app.
const app = express();

// Usando um middleware
app.use(express.json());

// Criando o próprio middleware
const log = (req,res,next) => {
    console.log(req.body);
    next();
}
app.use(log)

// Middleware de registro simples
app.use((req, res, next) => {
    console.log(`[${new Date().toLocaleString()}] ${req.method} ${req.url}`);
    next(); // Continue para o próximo middleware ou rota
  });


// DEFININDO ROTAS COM O EXPRESS
app.get('/', (req,res) => {
    res.send('<h1>Lista de tarefas</h1>');
})

app.get('/lugar', (req,res) => {
    res.send('<h1>Rota em lugar.</h1>');
})

app.get('/json', (req,res) => {
    res.json({title: "Listagem completa", done: "false"});
})

// Pegando o id do produto como parâmetro
app.get('/produto/:id', (req,res) => {
    const idProduto = req.params.id
    res.send(`<p>O id do produto é ${idProduto}</p>`);
})

app.listen(3000, () => {
    console.log("Servidor no ar!");
})

