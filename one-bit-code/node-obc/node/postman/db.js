const Sequelize = require('sequelize');

const sequelize = new Sequelize('teste_postman', 'root_postman', '12345678', {
    dyalect: 'mysql',
    host: 'db4free.net',
    port: 3306
});

sequelize.authenticate()
.then(() =>{
    console.log("Conexão com o banco de dados Realizado com sucesso!");
})
.catch(() => {
    console.log("Não foi possível estabelecer a conexão com o banco de dados!");
})

module.exports = {
    Sequelize,
    sequelize
};