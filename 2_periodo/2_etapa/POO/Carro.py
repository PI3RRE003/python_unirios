class Carro():
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def mostrar_informacoes(self):
        print(f"Marca:{self.marca}"
              f"\nModelo:{self.modelo}"
              f"\nAno:{self.ano}")


uno = Carro("Fiat", "Uno", 1997)
uno.mostrar_informacoes()