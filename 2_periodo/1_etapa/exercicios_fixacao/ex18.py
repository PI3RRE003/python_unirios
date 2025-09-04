estoque_produtos = []
def valor_total_estoque():
    soma_estoque = 0
    for produto in estoque_produtos:
        soma_estoque += produto[1] 
    return f'Valor do estoque:{soma_estoque}'

def produto_mais_caro_mais_barato():
    mais_caro = estoque_produtos[0]
    mais_barato = estoque_produtos[0]

    for produto in estoque_produtos:
        if produto[1] > mais_caro[1]:
            mais_caro = produto
        if produto[1] < mais_barato[1]:
            mais_barato = produto
    return (f"Produto mais caro: {mais_caro[0]} - R${mais_caro[1]:.2f}\n"
            f"Produto mais barato: {mais_barato[0]} - R${mais_barato[1]:.2f}")

def produtos_abaixo_de_20():
    ...


def menu():
    for i in range(1,2):
        print(f'{i} Produto:')
        nome_produto = input('Digite o nome do produto: ')
        preço_produto = float(input('Digite o preço do produto: '))
        produto = [nome_produto, preço_produto]
        estoque_produtos.append(produto)










menu()
#print(valor_total_estoque())
print(produto_mais_caro_mais_barato())