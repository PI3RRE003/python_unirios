from Animal import Animal

class Gato(Animal):
    def __init__(self,nome,cor_pelo):
        super().__init__(nome)
        self.cor_pelo = cor_pelo

    def fazer_som(self):
        super().fazer_som()
        print("MIAAAAAAU")

xanin = Gato("xanin", "Amarelo")
xanin.fazer_som()