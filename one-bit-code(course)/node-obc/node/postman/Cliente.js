const db = require("./db");

const Cliente = db.sequelize.define('Clientes', {
    id_cliente: {
        type: database.Sequelize.INTEGER,
        autoIncrement: true,
        allowNull: false,
        primaryKey: true
    },
    nome_cliente: {
        type: database.Sequelize.STRING(30),
        allowNull: false
    },
    sobrenome_cliente: database.Sequelize.STRING(50),
    email_cliente: {
        type: database.Sequelize.STRING(100),
        allowNull: false,
        unique: true
    }
});

module.exports = Cliente;