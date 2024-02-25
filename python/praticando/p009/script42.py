# Introduzindo o conceito de Programação orientado a objeto

# Class
# Syntaxe

# Propriedades fixas a classe
class Computador:
    def __init__(self):
        self.marca = 'Asus'
        self.memoria_ram = '8gb'
        self.placa_de_video = 'Nvidia'

computador1 = Computador()
computador2 = Computador()
computador3 = Computador()

print(computador1.marca, computador1.memoria_ram, computador1.placa_de_video)
print(computador2.marca, computador2.memoria_ram, computador2.placa_de_video)
print(computador3.marca, computador3.memoria_ram, computador3.placa_de_video)

# _init_ é chamado de consultor e permite criar a funcionalidade inicial que a classe terá.
# self serve para acessar as propriedades ou metódos de uma instância

# Propriedades dinâmicas
class Computador:
    def __init__(self,marca,memoria_ram,placa_de_video):
        self.marca = marca
        self.memoria_ram = memoria_ram
        self.placa_de_video = placa_de_video
    pass    

computador1 = Computador('Asus', '8bg', 'Nvidia')
computador2 = Computador('Dell', '10gb', 'GeForce')
computador3 = Computador('Acer', '16gb', 'ATM')
print(computador1.marca, computador1.memoria_ram, computador1.placa_de_video)
print(computador2.marca, computador2.memoria_ram, computador2.placa_de_video)
print(computador3.marca, computador3.memoria_ram, computador3.placa_de_video)


# Para criar os metódos, será feito funções dentro da classe criada
class Computador:
    def __init__(self,marca,memoria_ram,placa_de_video):
        self.marca = marca
        self.memoria_ram = memoria_ram
        self.placa_de_video = placa_de_video
   

    def Ligar(self):
        print('Estou ligando!')
    
    def Desligar(self):
        print('Estou desligando!')
    
    def ExibirInformacoesDesteComputador(self):
        print(self.marca, self.memoria_ram, self.placa_de_video)

computador1 = Computador('Asus', '16gb', 'Nvidia')
computador1.Ligar()
computador1.Desligar()
computador1.ExibirInformacoesDesteComputador()

# Atributo de classe: É um atributo que é igual para todos os objetos pertencentes a aquela classe.
# Atributo de Instância: É uma atributo referente a especificidade de cada objeto, ou seja, é um atributo atrelado as características específicas do objeto.  
# cls para atributos de classe 