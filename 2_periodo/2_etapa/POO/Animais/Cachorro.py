from Animal import  Animal

class Cachorro(Animal):
    def __init__(self,nome,raca):
        super().__init__(nome)
        self.raca = raca

    def fazer_som(self):
        super().fazer_som()
        print(f"AU AU")

zaya = Cachorro("Zaya", "PitBull")
zaya.fazer_som()