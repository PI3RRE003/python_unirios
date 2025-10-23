class ContaBancaria():
    def __init__(self, numero_conta, titular, saldo=0):
        self.numero_conta = numero_conta
        self.titular = titular
        self._saldo = saldo

    def __str__(self):
        conta = (f"\nNumero da conta:{self.numero_conta}"
                 f"\nTitular:{self.titular}"
                 f"\nSaldo: R${self._saldo}")
        return conta

    def depositar(self, valor):
        if valor <= 0:
            print("Error: numero não pode ser negativo ou zero")
            return
        else:
            self._saldo += valor
            print(f"Valor: R${valor} depositado com sucesso")

    def sacar(self, valor):
        if valor <= 0:
            print("Error: numero não pode ser negativo ou zero")
            return
        elif valor <= self._saldo:
            print("Saldo insuficiente")
        else:
            self.saldo -= valor
            print(f"Saque: R${valor} realizado com sucesso")

    def get_saldo(self):
        saldo = f"Saldo Atual: R${self._saldo}"
        print(saldo)

conta = ContaBancaria(1, "vitor")
print(conta)
conta.depositar(10)
conta.get_saldo()
