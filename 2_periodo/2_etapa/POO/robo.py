class EnergiaInsuficienteError(Exception):
    pass

class Robo:
    def __init__(self, nome ,energia=100):
        self.nome = nome
        self.energia = energia

    def mover(self, distancia):
        energia_por_distancia = distancia * 10

        if self.energia >= energia_por_distancia:
            self.energia -= energia_por_distancia
            print( f"O {self.nome} se moveu {distancia}m")
        else:
            raise EnergiaInsuficienteError(
                f"Energia insuficiente para percorrer: {distancia}m - Energia atual:{self.energia}% Recarregue as baterias"
                )
        
    def __str__(self):
        return f"Robô: {self.nome} - Energia: {self.energia}%"
    

astroboy = Robo(nome='Astroboy',energia=100)

try:
    print("Iniciando a missão do Astroboy...")
    astroboy.mover(7)
    print(astroboy)

    print("\nPróxima etapa da missão...")
    astroboy.mover(9) 
    print(astroboy)

    print('\nMissão concluida com sucesso')
except EnergiaInsuficienteError as e:
    print(f'\nA MISSÃO FALHOU: {e}')