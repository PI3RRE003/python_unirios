precos = []
print('PREÇOS:')
for i in range(1,4):
    print(f'{i} preço')
    preco = float(input('Digite o preço:'))
    precos.append(preco)

total = 0 #substitui sum(precos)
quantidade_acima_50 = 0
menor_preco = precos[0]#primeiro numero e 0
indice_menor = 0

for i in range(len(precos)):#ve o tamanho da lista
    preco = precos[i]
    total += preco

    if preco > 50:
        quantidade_acima_50 += 1

    if preco < menor_preco:
        menor_preco = preco
        indice_menor = i

print(f'\nTotal da compra: R${total:.2f}')
print(f'Quantidade de preços acima de R$50: {quantidade_acima_50}')
print(f'Menor preço digitado: R${menor_preco:.2f} (posição {indice_menor + 1})')
