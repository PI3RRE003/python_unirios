cidades = []
numero_populacao = []
escolas_publicas = []
proporcoes = []

print('========== Pesquisa Sobre Cidades ==========')
for i in range(1, 4):
    nome_cidade = input(f'\nDigite o nome da cidade {i}: ')
    cidades.append(nome_cidade)

    populacao = int(input(f'Digite a população da cidade {nome_cidade}: '))
    numero_populacao.append(populacao)

    numero_escolas_publicas = int(input(f'Digite o número de escolas públicas em {nome_cidade}: '))
    escolas_publicas.append(numero_escolas_publicas)

for i in range(len(cidades)):
    if numero_populacao[i] == 0:
        proporcao = 0
    else:
        proporcao = escolas_publicas[i] / numero_populacao[i]
    proporcoes.append(proporcao)

maior_proporcao = max(proporcoes)
indice_maior = proporcoes.index(maior_proporcao)

print('\n========================================')
print(f"A cidade com maior número de escolas por habitante é: {cidades[indice_maior]}")
print(f"Proporção: {maior_proporcao:.6f} escolas por habitante")

soma_escolas = 0
quantidade_cidades = 0

for i in range(len(cidades)):
    if numero_populacao[i] > 50000:
        soma_escolas += escolas_publicas[i]
        quantidade_cidades += 1

if quantidade_cidades > 0:
    media_escolas = soma_escolas / quantidade_cidades
    print(f"\nMédia de escolas públicas entre cidades com mais de 50.000 habitantes: {media_escolas:.2f}")
else:
    print("\nNenhuma cidade com mais de 50.000 habitantes foi registrada.")
