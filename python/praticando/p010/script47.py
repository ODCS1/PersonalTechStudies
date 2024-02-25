# Metódo de classe

class Usuario:
    cargo = 'usuario'

    def __init__(self, nome, idade, altura):
        self.altura = altura

    @classmethod
    def cargo_usuario(cls):
        print(cls.cargo)


Usuario.cargo_usuario()

# No metódo de classe com "@classmethod", a função logo abaixo tem acesso aos atributos de classe, assim eu não preciso ter instanciado o obejeto para que dê certo, pois o atributo é de classe, ou seja, um atributo geral para todos os objetos provenientes da mesma classe.