cidade = []
habitantes = []
obitos = []
taxa_mort = []
media_habitantes_total = []

for i in range(1,3):
    nome_cidade = input('\nDigite o nome da sua cidade: ')
    cidade.append(nome_cidade)

    numero_habitantes = int(input('Digite o numero de habitantes: '))
    habitantes.append(numero_habitantes)

    numero_obito_ano = int(input('Digite a quantidade de obitos no ano: '))
    obitos.append(numero_obito_ano)

for i in range(len(cidade)):
    taxa_mortalidade = (obitos[i]*1000) / habitantes[i]
    taxa_mort.append(taxa_mortalidade)

maior_taxa_mort = max(taxa_mort)
indice_maior = taxa_mort.index(maior_taxa_mort)

menor_taxa_mort = min(taxa_mort)
indice_menor = taxa_mort.index(menor_taxa_mort)

print(f'A cidade com maior taxa de mortalidade é:{cidade[indice_maior]}')
print(f'A cidade com menor taxa de mortalidade é:{cidade[indice_menor]}')

soma_populacao = sum(habitantes)
media_populacao = soma_populacao / len(habitantes)


print(f'A média de habitantes de todas as cidades juntas são:{media_populacao}')

soma_obitos = 0
quantidade_cidades = 0

for i in range(len(cidade)):
    if habitantes[i] > 50000:
        soma_obitos += obitos[i]
        quantidade_cidades +=1

if quantidade_cidades > 0:
    acima_media = soma_obitos/quantidade_cidades
    print(f'A média de obitos em cidades acima de 50 mil habitantes é: {acima_media:.2f}')
