const Sequelize = require('sequelize');
const sequelize = new Sequelize('test', 'root', '123456', {
    dialect: 'mysql',
    host: 'localhost',
    // port: 1433 SQL SERVER
    // port: 3306 //mysql
});

sequelize.authenticate()
.then(() => {
    console.log("Conexão com o banco de dados foi realizada com sucesso!");
}).catch(() => {
    console.log("ERRO: Não foi possível realizar a conexão com o banco de dados!");
})

const Postagem = sequelize.define('postagens', {
    titulo: {
        type: Sequelize.STRING
    },
    conteudo: {
        type: Sequelize.TEXT
    }
})

// Postagem.sync({force: true})

const Usuario = sequelize.define('usuario', {
    nome: {
        type: Sequelize.STRING
    },
    sobrenome: {
        type: Sequelize.STRING
    },
    idade: {
        type: Sequelize.INTEGER
    },
    email: {
        type: Sequelize.STRING
    }
})

// Usuario.sync({force: true})

Postagem.create({
    titulo: 'Postagem1',
    conteudo: 'conteudo qualquer'
})

module.exports = sequelize;