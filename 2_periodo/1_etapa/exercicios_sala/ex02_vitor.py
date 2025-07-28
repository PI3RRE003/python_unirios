nomes = []
idades = []
idades_maior_25 = []
for i in range(1,3):
    print('MÉDIA IDADES:')
    print(f'{i} Pessoa:')
    nome = input('Digite seu nome:')
    nomes.append(nome)
    idade = int(input('Digite sua idade:'))
    idades.append(idade)

for j in idades:
    if j > 25:
        nome_maior_25 = nomes[idades.index(j)]
        idades_maior_25.append(j)


media = sum(idades)/len(idades)

print(f'Pessoas com idade maior que 25:{nome_maior_25}')
print(f'Todas as idades:{idades}')
print(f'Média das idades:[{media}]')