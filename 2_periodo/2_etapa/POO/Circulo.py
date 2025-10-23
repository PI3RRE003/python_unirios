import math
class Circulo():
    def __init__(self, raio):
        if not isinstance(raio, (int, float)):
            raise TypeError("O raio deve ser um numero")

        if raio <= 0:
            raise ValueError("O raio deve ser positivo")
        self.raio = raio


    def calcular_area(self):
        area = math.pi * (self.raio**2)
        return area

    def calcular_circuferencia(self):
        circuferencia = 2 * math.pi * self.raio
        return circuferencia


try:
    circulo = Circulo(5)
    circuferencia = circulo.calcular_circuferencia()
    area = circulo.calcular_area()

    print(f"Area do circulo:{area}")
    print(f"Circuferencia do circulo:{circuferencia}")
    
except ValueError as e:
    print(f"Erro ao criar circulo:{e}")
except TypeError as e:
    print(f"Erro de tipo ao criar circulo:{e}")

