class Retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def calcula_area(self):
        area = self.largura * self.altura
        return f'A área do retangulo é: {area}'
    
    def calula_perimetro(self):
        perimetro = 2 * (self.largura + self.altura)
        return f'O perimetro do retangulo é: {perimetro}'
    
r1 = Retangulo(2,2)
print(r1.calcula_area())
print(r1.calula_perimetro())