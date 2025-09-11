class ContaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self,valor):
        self.saldo += valor
    
    def sacar(self, valor):
        if self.saldo < valor:
            return f"Saldo insuficiente: {self.saldo}"
        else:
            self.saldo -= valor
            return f"Saque realizado: {valor}"
    
    def __str__(self):
        return f'Conta de: {self.titular} - Saldo: R${self.saldo}'


c1 = ContaBancaria('Vitor',0)
c1.depositar(100)
print(c1)
print(c1.sacar(50))
print(c1)
        