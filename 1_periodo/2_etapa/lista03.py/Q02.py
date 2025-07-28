valor_compra_ate_100 = 0
desconto_10 = 0
valor_com_desconto_10 = 0

valor_compra_ate_500 = 0
desconto_12 = 0
valor_com_desconto_12 = 0

valor_compra_acima_500 = 0
desconto_15 = 0
valor_com_desconto_15 = 0

for compra in range(1,3):
    print('\nDesconto conforme a faixa:')
    valor_compra = float(input(f'{compra} Compra\nDigite o valor:'))

    if valor_compra <= 100:
        percentual = 0.10
        valor_compra_ate_100 += valor_compra
        desconto = (valor_compra*percentual)
        valor_com_desconto = valor_compra - (valor_compra*percentual)
        desconto_10 += desconto
        valor_com_desconto_10 = valor_com_desconto
    elif valor_compra > 100 and valor_compra < 500:
        percentual = 0.12
        valor_compra_ate_500 += valor_compra
        desconto = (valor_compra*percentual)
        valor_com_desconto = valor_compra - (valor_compra*percentual)
        desconto_12 += desconto
        valor_com_desconto_12 = valor_com_desconto
    elif valor_compra > 500:
        percentual = 0.15
        desconto = (valor_compra*percentual)
        desconto_15 += desconto
        valor_compra_acima_500 += valor_compra
        valor_com_desconto = valor_compra - (valor_compra*percentual)
        valor_com_desconto_15 = valor_com_desconto

if desconto_10 != 0:
    print(f'\nPDV\nValor original:{valor_compra_ate_100}\nPercentual de desconto:{desconto_10}\nValor com desconto:{valor_com_desconto_10}')
if desconto_12 != 0:
    print(f'\nPDV\nValor original:{valor_compra_ate_500}\nPercentual de desconto:{desconto_12}\nValor com desconto:{valor_com_desconto_12}')
if desconto_15 != 0:
    print(f'\nPDV\nValor original:{valor_compra_acima_500}\nPercentual de desconto:{desconto_15}\nValor com desconto:{valor_com_desconto_15}')