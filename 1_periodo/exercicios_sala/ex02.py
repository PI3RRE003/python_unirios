eletros = ["Geladeira", "Ar-condicionado",]
consumos = []

for i in range(1,6):
    print('Eletrodomestico',i)
    nome = input('Informe o nome do eletrodomestico: ')
    consumo = float(input('Informe o consumo mensal em kw/h: '))
    eletros.append(nome)
    consumos.append(consumo)

mais_economico = eletros[consumos.index(min(consumos))]
media = sum(consumos)/5
qtd = 0 
for i in consumos:
    if i > 100:
        qtd+=1

print(f'O eletrodomestico mais economico é {mais_economico}')
print(f'a media de consumo foi de {media}')
print(f'A quantidade de eletros que consomem acima de 100 kwh mês e {qtd}')