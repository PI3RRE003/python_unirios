nomes = []
populacoes = []
numero_escolas_publicas = []

for i in range(1,4):
    nome = input('Digite o nome da cidade: ')
    nomes.append(nome)

    populacao = int(input(f'Digite a polupação de {nome}: '))
    populacoes.append(populacao)

    escolas = int(input(f'Digite o numero ed escolas de {nome}: '))
    numero_escolas_publicas.append(escolas)

numero_escolas_habitante = sum(numero_escolas_publicas) / sum(populacoes)
print(f'A cidade com maior número de escolas por habitante: {numero_escolas_habitante}')

media = sum(populacoes)/len(populacoes)

media_alta = []

for i in range(len(populacoes)):
    if populacoes[i] > 50000:
        media_alta.append(nome)
        media_alta.append(media)

if nome:
    for i in range(len(nomes)):
        print(f'media de eescolas entre cidades com mais de 50000 habitantes:\n {media_alta}')
else:
    print('Nenhuma ciadde encontrada')