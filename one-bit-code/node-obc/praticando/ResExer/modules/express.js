const express = require('express');
const porta = 3000;
const app = express();

// CONFIGURANDO CAMINHO ARQUIVOS
app.use(express.static("arquivos"));

// CONFIGURANDO EJS
app.set("views", "./view");
app.set("view engine", "ejs");


// ROTAS
app.get("/home", (req,res) => {
    res.render("home");
});

app.get("/calculadora", (req,res) => {
    res.render("calculadora");
});

app.get("/vitrine", (req,res) => {
    res.render("vitrine");
});


app.listen(porta, () => {
    console.log(`Porta 3000 ativo.`);
});