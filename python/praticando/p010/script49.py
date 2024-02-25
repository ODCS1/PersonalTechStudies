# Herança e sobreposição

class Pessoa:
    def __init__(self, nome, cpf, altura):
        self.nome = nome
        self.cpf = cpf
        self.altura = altura
        print('Teste')

    def exibe_cpf(self, cpf):
        print(cpf) 

class Secretaria(Pessoa):
    def __init__(self, id_secretaria, nome, cpf, altura):
        super().__init__(nome, cpf, altura)
        self.id_secretaria = id_secretaria

class Vendedor(Pessoa):
    def __init__(self, total_vendas, nome, cpf, altura):
        super().__init__(nome, cpf, altura)
        total_vendas += 10
        self.total_vendas = total_vendas

secretaria1 = Secretaria('1', 'Maria', '12345678901', '173')
vendedor1 = Vendedor(27, 'Adalberto', '3267587523', '178')


secretaria1.exibe_cpf('12345678901')