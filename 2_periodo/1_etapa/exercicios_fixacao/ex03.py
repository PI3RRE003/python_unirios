def total_compra(dados):
    total = 0
    for preco in dados.values():
        total += preco
    print(f'Gasto Total:{total}')    

def produto_acima_50(dados):
    print('Produtos Acima de 50:')
    for produto, preco in dados.items():
        if preco > 50:
            print(f'{produto} - {preco}')

def menor_preco(dados):
    print('Produto mais barato')
    menor_preco = 0
    menor_produto = ''
    for produto, preco in dados.items():
        if menor_preco is None or preco < menor_preco:
            menor_preco = preco
            menor_produto = produto
    print(f'{menor_produto} - {menor_preco}')


produtos = {}
for i in range(1,3):
    nome_produto = input('\nDigite o nome do produto:')
    preco_produto = int(input('Digite o preço do produto:'))
    produtos[nome_produto] = preco_produto
    

#total_compra(produtos)
#produto_acima_50(produtos)
menor_preco(produtos)