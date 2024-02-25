class Produto{
    constructor () {
        this.id = 0
        this.nomeProduto = ''
        this.valor = 0
    }

    adicionar () {
        alert('Vamos adicionar um produto!')

        // Regras de negócio...
    }

    excluir () {
        // Regras de negócio ...

        alert('Vamos excluir esse produto!')
    }
}

var produto = new Produto()