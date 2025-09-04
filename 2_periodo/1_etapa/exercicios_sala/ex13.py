def imposto_e_roubo(nome, preco):
    if preco > 200:
        imposto = (preco * 0.10)
        qtd_imposto = '10%'
        valor_taxado = preco + imposto
    else:
        imposto = (preco * 0.05)
        qtd_imposto = '5%'
        valor_taxado = preco + imposto
    return f'\nNome do produto:{nome}\nPreço: R${preco:.2f}\nImposto:{qtd_imposto}\nPreço Final com imposto: R${valor_taxado:.2f}'

print('SEFAZ TAXANDO PRODUTO:')
nome_produto = input('Produto: ')
preco_produto = float(input('Preço do produto: R$'))

print(imposto_e_roubo(nome_produto,preco_produto))