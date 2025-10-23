class Retangulo():
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def calcular_area(self):
        area =  self.largura * self.altura
        return area

    def calcular_perimetro(self):
        perimetro = (2 * self.largura + self.altura)
        return perimetro


retangulo = Retangulo(10, 5)
area = retangulo.calcular_area()
perimetro = retangulo.calcular_perimetro()

print(f"A area do retangulo é: {area}")
print(f"O perimetro do retangulo é:{perimetro}")