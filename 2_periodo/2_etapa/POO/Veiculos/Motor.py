class Motor():
    def __init__(self,cilindrada,potencia):
        self.cilindrada = cilindrada
        self.potencia = potencia

    def __str__(self):
        motor = f"Motor:{self.cilindrada} - {self.potencia}CV"
        return motor