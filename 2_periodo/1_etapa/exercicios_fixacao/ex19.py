class Pessoa:
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade
    
    def apresentacao(self):
        return f"Olá meu nome é {self.nome} e tenho {self.idade} anos"

"""
nome = input('Digite seu nome: ')
idade = int(input('Digite sua idade: '))
pessoa = Pessoa(nome,idade)
print(pessoa.apresentacao())

"""
class Retangulo:
    def __init__(self,base,altura):
        self.base = base
        self.altura = altura

    def area(self):
        area = (self.base * self.altura)
        return f'A area do retangulo: {area}'
    
    def perimetro(self):
        perimetro = 2 * (self.base + self.altura)
        return f'O perimetro do retangulo é: {perimetro}'

'''    
base = int(input('Digite a base: '))
altura = int(input('Digite a altura: '))
retangulo_1 = Retangulo(base,altura)
print(retangulo_1.area())
print(retangulo_1.perimetro())
'''

class ContaBancaria:
    def __init__(self,titular,saldo):
        self.titular = titular
        self.saldo = saldo

    def depositar(self):
        valor = float(input('\nDigite a quantidade que deseja depositar: '))
        if valor > 0:
            (self.saldo) += valor
            return f'Valor depositado:{valor} - Saldo:{self.saldo}'
        return 'Valor inválido para deposito'
    
    def sacar(self):
        valor = float(input('\nDigite a quantidade que deseja sacar: '))
        if valor <= 0:
            return 'valor inválido para saque'
        if valor > self.saldo:
            return f'Saldo insuficiente! Saldo atual:{self.saldo:.2f}'
        self.saldo -= valor
        return f'Saque de {valor:.2f} realizado. saldo atual: {self.saldo:.2f}'

'''
conta_1 = ContaBancaria('Vitor', 100)
print(conta_1.depositar())
print(conta_1.sacar())
'''
