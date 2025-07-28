produto = []
preco_produto = []
quantidade_vendas = []

for i in range(1,4):

    nome = input('Digite o nome do produto: ')
    produto.append(nome)

    preco = float(input(f'Qual o preço de {nome}: '))
    preco_produto.append(preco)

    vendas = float(input(f'Digite a quantidade de vendas do produto {nome}: '))
    quantidade_vendas.append(vendas)

maior_faturamento = []
faturamento_produto = []

for i in range(len(quantidade_vendas)):
    if quantidade_vendas[i] > maior_faturamento:
        

