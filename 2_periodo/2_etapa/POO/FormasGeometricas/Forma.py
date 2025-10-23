import  math
"""
POO: HERANÇA,COMPOSIÇÃO E POLIMORFISMO
"""
class Forma():
    def __init__(self, nome):
        self.nome = nome

    def calcular_area(self):
        raise NotImplementedError("Subclasses devem implementar este metodo")


class Retangulo(Forma):
    def __init__(self, largura, altura):
        super().__init__("Retângulo")
        self.largura = largura
        self.altura = altura

    def calcular_area(self):
        area = self.largura * self.altura
        print(f"A area do {self.nome} é de:{area}\n")


class Circulo(Forma):
    def __init__(self,raio):
        super().__init__("Circulo")

        if raio <= 0:
            print("Error: raio não deve ser negativo ou zero")
        else:
            self.raio = raio


    def calcular_area(self):
        area = math.pi * (self.raio**2)
        print(f"A area do {self.nome} é de:{area:.2f'}\n")


formas = [
    Retangulo(10, 5),
    Circulo(7),
    Retangulo(4,4)
]

for forma in formas:
    print(forma.nome)
    forma.calcular_area()
