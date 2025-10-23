class Aluno():
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula
        self.notas = []

    def adicionar_nota(self,nota):
        if nota <= 0 or nota > 10:
            print("Error: Nota não pode ser menor que zero nem maior que dez")
            return
        elif len(self.notas) == 3:
            print("Aluno Já contem 3 notas, retorne e calcule a média")
            return
        else:
            self.notas.append(nota)
            print(f"Nota:{nota} adicionada com sucesso")

    def calcular_media(self):
        if len(self.notas) == 0:
            print("Error: Lista de notas vazia retornando")
            return

        media = sum(self.notas)/ len(self.notas)
        return media

    def mostar_informacoes(self):
        media = self.calcular_media()
        aluno = (f"\nNome:{self.nome}"
                 f"\nMatricula:{self.matricula}"
                 f"\nNotas:{self.notas}"
                 f"\nMedia:{media:.2f}")
        print(aluno)

try:
    vitor = Aluno("Vitor","1")
    vitor.adicionar_nota(7)
    vitor.adicionar_nota(8)
    vitor.adicionar_nota(9)
    vitor.mostar_informacoes()
except Exception as e:
    print(f"Error:{e}")