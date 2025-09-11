class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def __str__(self):
        return f"Pessoa: {self.nome} - Idade: {self.idade}"
    '''
    def saudacao(self):
        return f'Olá meu nome é: {self.nome} e tenho {self.idade} Anos
    '''

class Estudante(Pessoa):
    def __init__(self, nome, idade, curso):
        super().__init__(nome,idade)

        self.curso = curso

    def __str__(self):
        info_pessoa = super().__str__()
        return f'{info_pessoa} - Curso: {self.curso}'        


p1 = Pessoa("Vitor", 22)
e1 = Estudante("Kawane", 20, "Sistemas da informação")
print(e1)