print('PDV')
print('1 - A VISTA\n2 - PRAZO')
op = int(input('Digite a opção de venda: '))

if op == 1:
    print('\nCompra a vista')
    valor = float(input('Digite o valor R$: '))
    desconto = (valor*0.05)
    valor_final = valor - desconto
    print(f'Valor final da compra a vista:{valor_final}')
elif op == 2:
    print('\nCompra a prazo')
    valor = float(input('Digite o valor R$: '))
    acrescimo = (valor*0.02)
    valor_final = valor + acrescimo
    print(f'Valor final da compra a prazo:{valor_final}')
    