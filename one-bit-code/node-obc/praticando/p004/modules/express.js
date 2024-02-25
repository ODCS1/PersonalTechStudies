const express = require('express');
const app = express();
const porta = 3000;

app.use(express.static("arquivos"));

app.set('view engine', 'ejs');


app.get("/home", (req,res) => {
    res.render("home");
});


app.listen(porta, () => {
    console.log(`Servidor na porta ${porta}.`)
})