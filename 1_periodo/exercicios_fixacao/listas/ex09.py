nomes = []
idades = []

for i in range(1,4):
    
    nome = input('Digite seu nome: ')
    nomes.append(nome)

    idade = int(input(f'{nome} digite sua idade: '))
    idades.append(idade)

mais_velha = max(idades)
indice_maior = nomes[idades.index(max(idades))]

mais_nova = min(idades)
indice_menor = nomes[idades.index(min(idades))]

media = sum(idades)/len(idades)

acima_media_nome = []
acima_media_idade = []

for i in range(len(idades)):
    if idades[i] > media:
        acima_media_nome.append(nomes[i])
        acima_media_idade.append(idades[i])

print(f'Pessoa mais velha:{indice_maior}, idade:{mais_velha}')
print(f'Pessoa mais nova:{indice_menor}, idade:{mais_nova}')
print(f'Média de idades:{media:.2f}')

if acima_media_nome:
    for i in range(len(acima_media_nome)):
        print(f'Pessoa com idade acima da média:{acima_media_nome[i]}, idade:{acima_media_idade[i]}')
else:
    print('Nenhuma idade acima da média')