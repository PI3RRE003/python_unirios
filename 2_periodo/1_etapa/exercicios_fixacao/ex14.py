class Funcionario:
    
    def __init__(self,nome,salario):
        self.nome = nome
        self.salario = salario


class Gerente(Funcionario):
    
    def aumenta_salario(self):
        aumento = (self.salario*0.10)
        sal_atualizado = (self.salario) + (self.salario*0.10)
        return f'Salario atualizado:{sal_atualizado} - Aumento:{aumento} '
    
p1 = Funcionario('Vitor',100)
g1 = Gerente('Kaw', 300)
print(g1.aumenta_salario(p1.salario))