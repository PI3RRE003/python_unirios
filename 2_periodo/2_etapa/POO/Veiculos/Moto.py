from Veiculo import Veiculo

class Moto(Veiculo):
    def __init__(self,marca, modelo, tipo):
        super().__init__(marca,modelo)
        self.tipo = tipo

    def mostrar_informacoes(self):
        super().mostrar_informacoes_base()
        print(f"Tipo da Moto:{self.tipo}")
