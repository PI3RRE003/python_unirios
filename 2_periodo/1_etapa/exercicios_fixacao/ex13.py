class Cachorro:
    def __init__(self,nome,som):
        self.nome = nome
        self.som = som

    def latir(self):
        return f'O Cachorro {self.nome} fez: {self.som}'
    
cachorro = Cachorro('Nala','AuAu')
print(f'{cachorro.latir()}')