const express = require('express');
const app = express();
const porta = 3000;


app.get('/', (req,res) => {
    res.render('home');
});

app.post('/cadastro', async (req,res) => {
    
});

app.listen(porta, () => {
    console.log(`Servidor ON em http://localhost:${porta}`)
})