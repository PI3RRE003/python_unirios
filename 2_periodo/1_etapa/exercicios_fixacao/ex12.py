class ContaBancaria:
    def __init__(self,titular,saldo):
        self.titular =titular
        self.saldo = saldo

    def depositar(self,valor):
        self.saldo += valor
        return f'{valor} Depositado com sucesso!'
    
    def sacar(self, valor):
        if valor > self.saldo:
            return f'Saldo insuficiente, Saldo atual:{self.saldo}'
        self.saldo -= valor 
        return f'{valor} Saque realizado com sucesso!'
    
    def get_saldo(self):
        return f'Saldo atual de {self.titular}: R$:{self.saldo}'
    
vitor = ContaBancaria('Vitor Pierre', 0)
print(f'{vitor.depositar(20)}')
print(f'{vitor.sacar(10)}')
print(f'{vitor.get_saldo()}')
