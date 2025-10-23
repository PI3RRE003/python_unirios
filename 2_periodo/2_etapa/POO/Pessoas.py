class Pessoa():
    contador_pessoas = 0
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        Pessoa.contador_pessoas+=1

    def apresentar(self):
        print(f"Nome:{self.nome}"
              f"\nIdade:{self.idade}")




vitor = Pessoa("Vitor", 22)
kawane = Pessoa("Kawane", 20)

vitor.apresentar()
kawane.apresentar()
print(f"Total de pessoas contadas: {Pessoa.contador_pessoas}")