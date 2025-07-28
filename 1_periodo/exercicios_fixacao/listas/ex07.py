nome_produto = []
preco_produto = []

for i in range(1, 6):  # 5 produtos
    produto = input(f'\nDigite o nome do {i}º produto: ')
    nome_produto.append(produto)

    preco = float(input('Digite o preço: '))
    preco_produto.append(preco)

mais_caro = max(preco_produto)
indice_maior = nome_produto[preco_produto.index(mais_caro)]

mais_barato = min(preco_produto)
indice_menor = nome_produto[preco_produto.index(mais_barato)]

media = sum(preco_produto) / len(preco_produto)

acima_media_nomes = []
acima_media_precos = []

for i in range(len(preco_produto)):
    if preco_produto[i] > media:
        acima_media_nomes.append(nome_produto[i])
        acima_media_precos.append(preco_produto[i])

print(f'\nProduto mais caro: {indice_maior}, Valor: R$ {mais_caro:.2f}')
print(f'Produto mais barato: {indice_menor}, Valor: R$ {mais_barato:.2f}')
print(f'Média de preços: R$ {media:.2f}')

print('\n--- Produtos acima da média ---')
if acima_media_nomes:
    for i in range(len(acima_media_nomes)):
        print(f'{acima_media_nomes[i]} - R$ {acima_media_precos[i]:.2f}')
else:
    print('Nenhum produto acima da média.')
