carros =[]
consumos =[]

for i in range(1,4):
    carro = input('Digite o nome do seu carro: ')
    carros.append(carro)

    consumo = float(input('Quantos km/l o {carro} faz? '))
    consumos.append(consumo)

maior_consumo = max(consumos)
menor_consumo = min(consumos)

indic_maior = carros[consumos.index(max(consumos))]
indic_menor= carros[consumos.index(min(consumos))]

media = sum(consumos)/len(consumos)

print(f'Carro que mais consome:{indic_maior}, consumo: {maior_consumo}')
print(f'Carro que menos consome:{indic_menor}, consumo: {menor_consumo}')
print(f'Média de consumo dos carros:{media}')

# funciona mas a expressão das variaveis estão contraditorias ao que devem ser