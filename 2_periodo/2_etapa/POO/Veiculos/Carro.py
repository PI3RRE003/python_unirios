from Veiculo import Veiculo
from Motor import Motor

class Carro(Veiculo):
    def __init__(self, marca, modelo, numero_portas, cilindrada_motor, potencia_motor):
        super().__init__(marca,modelo)
        self.numero_portas = numero_portas
        self.motor = Motor(cilindrada_motor, potencia_motor)

    def mostrar_informacoes(self):
        super().mostrar_informacoes_base()
        print(f"Numero de portas:{self.numero_portas}"
              f"\n{self.motor}")

carro = Carro("Fiat","Uno",4,1.0,100)
carro.mostrar_informacoes()