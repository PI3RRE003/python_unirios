from datetime import date

def obterData():
    data_atual = date.today()
    return data_atual.strftime('%d/%m/%Y')


def emitir_venda(nome,preco):
    if preco > 100:
        desconto = '15%'
        valor_final = preco - (preco * 0.15)
    else:
        desconto = '10%'
        valor_final = preco - (preco * 0.10) 

    data = obterData()
    return f'Info Venda:\n{data}\nProduto:{nome}\nPreço: R${preco}\ndesconto:{desconto}\nValor com desconto:{valor_final}'   
#print(obterData())

def calcula_imposto(preco):
    if preco > 500:
        valor = preco + (preco * 0.3)
    else:
        valor = preco + (preco * 0.1)
    return valor

nome_produto = input('Digite o nome do produto: ')
preco_produto = float(input('Digite o preço do produto: '))

print(emitir_venda(nome_produto,calcula_imposto(preco_produto)))