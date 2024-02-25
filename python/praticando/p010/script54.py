

class ContaCorrente:
    def __init__(self, numero, saldo):
        self.numero = numero
        self.saldo = saldo
    
    def depositar(self, valor):
        self.saldo += valor
    
    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
        else:
            print("Saldo insuficiente.")

    def consultar_saldo(self):
        return self.saldo


class CartaoAlimentacao:
    def __init__(self, numero, saldo):
        self.numero = numero
        self.saldo = saldo
    
    def adicionar_credito(self, valor):
        self.saldo += valor
    
    def usar_cartao(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
        else:
            print("Saldo insuficiente.")

    def consultar_saldo(self):
        return self.saldo


class CartaoCredito:
    def __init__(self, numero, limite):
        self.numero = numero
        self.limite = limite
        self.saldo_devido = 0
    
    def fazer_compra(self, valor):
        if self.saldo_devido + valor <= self.limite:
            self.saldo_devido += valor
        else:
            print("Limite de crédito excedido.")

    def efetuar_pagamento(self, valor):
        if valor <= self.saldo_devido:
            self.saldo_devido -= valor
        else:
            print("Valor do pagamento excede o saldo devido.")

    def consultar_saldo_devido(self):
        return self.saldo_devido


class Data:
    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano

    def exibir_data(self):
        return f"{self.dia}/{self.mes}/{self.ano}"


class Hora:
    def __init__(self, hora, minuto, segundo):
        self.hora = hora
        self.minuto = minuto
        self.segundo = segundo
    
    def exibir_hora(self):
        return f"{self.hora}:{self.minuto}:{self.segundo}"


class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def exibir_coordenadas(self):
        return f"({self.x}, {self.y})"



class Reta:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
    
    def calcular_comprimento(self):
        dx = self.x2 - self.x1
        dy = self.y2 - self.y1
        return (dx ** 2 + dy ** 2) ** 0.5




class Cliente:
    def __init__(self, nome, endereco, telefone):
        self.nome = nome
        self.endereco = endereco
        self.telefone = telefone
    
    def exibir_informacoes(self):
        return f"Nome: {self.nome}\nEndereço: {self.endereco}\nTelefone: {self.telefone}"


class Livro:
    def __init__(self, titulo, autor, ano_publicacao):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
    
    def exibir_informacoes(self):
        return f"Título: {self.titulo}\nAutor: {self.autor}\nAno de Publicação: {self.ano_publicacao}"


class EmprestimoLivros:
    def __init__(self, livro, cliente, data_emprestimo, data_devolucao):
        self.livro = livro
        self.cliente = cliente
        self.data_emprestimo = data_emprestimo
        self.data_devolucao = data_devolucao
    
    def exibir_detalhes_emprestimo(self):
        return f"Livro emprestado:\n{self.livro}\n\nCliente:\n{self.cliente}\n\nData de Empréstimo: {self.data_emprestimo}\nData de Devolução: {self.data_devolucao}"
