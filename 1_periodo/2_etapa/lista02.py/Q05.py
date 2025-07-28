while True:
    print('Desconto prograssivo')
    preco = float(input('Digite o preço unitario do produto:'))
    qtd = int(input('Digite a quantidade:'))

    if qtd == 10:
        mensagem = 'Sem desconto'
    elif qtd > 10 and qtd < 50:
        desconto = 0.05
        mensagem =  '5% de desconto'
        valor_sem_desconto = preco * qtd
        valor_com_desconto = valor_sem_desconto-(valor_sem_desconto * desconto)
        valor_final = valor_com_desconto
    elif qtd > 50 and qtd < 100:
        desconto = 0.10
        mensagem =  '10% de desconto'
        valor_sem_desconto = preco * qtd
        valor_com_desconto = valor_sem_desconto-(valor_sem_desconto * desconto)
        valor_final = valor_com_desconto
    elif qtd > 100:
        desconto = 0.15
        mensagem =  '15% de desconto'
        valor_sem_desconto = preco * qtd
        valor_com_desconto = valor_sem_desconto-(valor_sem_desconto * desconto)
        valor_final = valor_com_desconto
    
    print(f'\nPDV:\nPreço unitario do produto:{preco}\nPreço original:{valor_sem_desconto}\nQuantidade:{qtd}\nDesconto:{mensagem}\nValor final:{valor_final}\n')