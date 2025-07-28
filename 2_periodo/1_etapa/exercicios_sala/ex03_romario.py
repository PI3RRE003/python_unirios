precos = []
for i in range(1,6):
    print(f'{i} Produto:')
    preco = float(input('Digite o preço:'))
    precos.append(preco)

total = sum(precos)
menor = min(precos)

print(f'Total de compras: R$:{total}')
print(f'Menor preço R$:{menor}')
print(f'Produtos acima de R$50:')
for preco in precos:
    if preco> 50:
        indice = precos.index(preco)
        print(f'Produto: {indice}')

