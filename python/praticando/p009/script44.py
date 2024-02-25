

class Usuario:
    cargo = 'usuario'

    def __init__(self, nome, idade, altura):
        self.nome = nome
        self.idade = idade
        self.altura = altura

    def altura_usuario(self):
        print(self.altura)

    def exibe_cargo(self):
        print(f'Cargo do {self.nome}: {self.cargo}')

usuario1 = Usuario('Caio', '21', '173')
usuario2 = Usuario('Marcos', '31', '180')

usuario1.exibe_cargo()
usuario2.exibe_cargo()