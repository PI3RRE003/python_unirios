class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def exibir_dados(self):
        return (f'Nome: {self.nome} - Idade: {self.idade}')

nome_pessoa_1 = input('Digite um nome: ')
idade_pessoa_1 = int(input('Digite uma idade: '))
p1 = Pessoa(nome_pessoa_1, idade_pessoa_1)
print(Pessoa.exibir_dados(p1))