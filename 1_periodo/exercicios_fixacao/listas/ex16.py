cidade = []
numero_habitantes = []
numero_acidentes_ano = []

for i in range(1,3):

    nome = input('Digite o nome de sua cidade: ')
    cidade.append(nome)

    habitantes = int(input(f'Digite o numerod de habitantes de {nome}: '))
    numero_habitantes.append(habitantes)

    acidentes = int(input('Digite a quantidade de acidentes por ano: '))
    numero_acidentes_ano.append(acidentes)

mais_acidente = max(numero_acidentes_ano)
indice_maior = cidade[numero_acidentes_ano.index(max(numero_acidentes_ano))]

cidade_maiscem = []

for i in range(len(numero_habitantes)):
    if numero_habitantes[i] > 100000:
        media_acidente = sum(cidade_maiscem)/len(cidade_maiscem)
        cidade_maiscem.append(nome)
        cidade_maiscem.append(media_acidente)

print(f'Cidade com maior indice de acidente por pessoa:{indice_maior}, quantidade:{mais_acidente}')

if cidade:
    for i in range(len(cidade)):
        print(f'media de acidentes entre as cidades com mais de 10000 habitantes{cidade_maiscem}')
else:
    print('Nenhuma cidade')