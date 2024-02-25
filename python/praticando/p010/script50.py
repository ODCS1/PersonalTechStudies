#calculadora.py
class Calculadora:

    def __init__(self, param1, param2):
        self.a = param1
        self.b = param2

    def soma(self):
        return self.a + self.b

    def subtrai(self):
        return self.a - self.b

    def multiplica(self):
        return self.a * self.b

    def divide(self):
        return self.a / self.b

class num:
    def __init__(self, a, b):
        
        pass
  

# a = int(input('Digite o 1° valor: '))
# b = int(input('Digite o 2°valor: '))


def valores():
    param1 = int(input('Digite o 1° número: '))
    param2 = int(input('Digite o 2° número: '))
    operacao(param1, param2)

def operacao(param1, param2):
    operacao = input('Qual operação que você deseja fazer? \nSOMA[som] \nSubtração[sub] \nMultiplicação[mult] \nDivisão[divi] \nEsolha: ')
    
    if operacao == 'som':
        Calculadora(param1, param2)
        Calculadora.soma(param1, param2)

valores()