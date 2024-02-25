const Sequelize = require('sequelize')

const sequelize = new Sequelize('postapp', 'root', '123456', {
    dialect: 'mysql',
    host: 'localhost'
    // port: 1433 SQL SERVER
    // port: 3306 //mysql
});


module.exports = {
    Sequelize: Sequelize,
    sequelize: sequelize
}