class Carro:
    def __init__(self,marca,modelo,ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def exibir_info(self):
        return f'Marca:{self.marca} - Modelo:{self.modelo} - Ano:{self.ano}'

corola = Carro('Toyota','Corolla', 2025)       
print(corola.exibir_info())

orochi = Carro('Renaut', 'Orochi', 2016)
print(orochi.exibir_info())

strada = Carro('Fiat','Strada Ranch', 2025)
print(strada.exibir_info())