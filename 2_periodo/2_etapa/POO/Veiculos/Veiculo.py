class Veiculo():
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def mostrar_informacoes_base(self):
        veiculo = (f"\nMarca:{self.marca}"
                   f"\nModelo:{self.modelo}")
        print(veiculo)



"""
POO: HERANÇA E COMPOSIÇÃO
"""



