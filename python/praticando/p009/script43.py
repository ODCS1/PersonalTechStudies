# Criar classe carro e no mínimo 3 propriedades para a classe carro e no mínimo 3 métodos para ela.


class Carro:
    def __init__(self, nome, cor, marca):
        self.nome = nome
        self.cor = cor
        self.marca = marca
    def Andar(self):
        print('Estou andando!')
    def freiar(self):
        print('Freiar!')
    def estacionar(self):
        print('Estacionando!')

carro = Carro('Uno', 'Cinza', 'Fiat')
print(carro.nome, carro.cor, carro.marca)

carro.Andar()
carro.freiar()
carro.estacionar()

