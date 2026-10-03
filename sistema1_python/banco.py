class Conta:
    def __init__(self, saldo=0):
        self.saldo = saldo
    def depositar(self, valor):
        if valor <= 0:
            raise ValueError("Valor inválido")
        self.saldo += valor
    def sacar(self, valor):
        if valor > self.saldo:
            raise ValueError("Saldo insuficiente")
        self.saldo -= valor
