(async () => {

    const database = require("./db");
    const Produto = require("./models/produto");
    await database.sync();

    // OPERAÇÕES NO BANCO DE DADOS SÃO ASSÍNCRONAS, POR ISSO O USO DO AWAIT

    // ----------------------------------------
    // CRIANDO UM NOVO ELEMENTO
    // const novoProduto = await Produto.create({
    //     nome: 'Ryzen 7 5700x',
    //     preco: 150,
    //     descricao: 'Processador AMD'
    // })
    // console.log(novoProduto);
    // ---------------------------------------

    // ----------------------------------------
    // BUSCAR ELEMENTOS PELO VALOR DA PK
    // const produtos = await Produto.findByPk(1);
    // ----------------------------------------

    // ----------------------------------------
    // BUSCAR TODOS OS ELEMENTOS DE UMA TABELA
    // const produtos = await Produto.findAll();
    // ----------------------------------------

    // ----------------------------------------
    // BUSCAR ELEMENTOS USANDO O WHERE
    // const produtos = await Produto.findAll({
    //     where: {
    //       preco: 30
    //     }
    // });
    // ----------------------------------------

    // const produto = await Produto.findByPk(1);
    // console.log(produto);

    // ----------------------------------------
    // DELETANDO UM ELEMENTO DA TABELA
    // await produto.destroy();
    // ----------------------------------------

    // ----------------------------------------
    // DELETANDO DE UMA VEZ
    // await Produto.destroy({ where: {
    //     preco: 30
    // }})
    // ----------------------------------------

    // ----------------------------------------
    // ALTERANDO ELEMENTO
    // produto.descricao = 'Alterado!!!';
    // await produto.save();
    // ----------------------------------------

})();
