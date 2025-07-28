carros = []
consumo = []

for i in range(1,4):
    print('========== Carro mais economico ==========')
    carro = input('Digite a marca de seu carro: ')
    carros.append(carro)

    consumo_km = float(input('Digite quantos km faz com um litro: '))
    print('\n')
    consumo.append(consumo_km)

mais_economico = carros[consumo.index(max(consumo))]
print(f'O Carro mais economico é:{mais_economico}')