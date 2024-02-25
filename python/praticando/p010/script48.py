# Metódo Estático

class Usuario:
    cargo = 'usuario'

    def __init__(self,altura):
        self.altura = altura

    @staticmethod
    def e_adulto(idade):
        if idade > 17:
            print(True)
        else:
            print(False)


Usuario.e_adulto(17)

# Pode usar o metódo estático desde que dentro deste metódo não será necessário: saber quais são os atributos de classe, chamar uma função de instância, atributos de instância, metódo de classe.