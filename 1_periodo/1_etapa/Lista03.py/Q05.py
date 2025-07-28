print('Aumento de preço dos produtos')
nome = input('Digite o nome do produto: ')
preco = float(input('Digite o preço do produto: '))

if preco < 50:
    aumento = 0.05
    valor_aumento = preco*aumento
    novo_preco = preco+valor_aumento
    mensagem = f'O produto {nome} custava R$:{preco}, sofreu um aumento de 5% e agora custa R$:{novo_preco}'
elif preco >= 50 and preco <= 200:
    aumento = 0.15
    valor_aumento = preco*aumento
    novo_preco = preco+valor_aumento
    mensagem = f'O produto {nome} custava R$:{preco}, sofreu um aumento de 15% e agora custa R$:{novo_preco}'
elif preco > 200:
    aumento = 0.10
    valor_aumento = preco*aumento
    novo_preco = preco+valor_aumento
    mensagem = f'O produto {nome} custava R$:{preco}, sofreu um aumento de 10% e agora custa R$:{novo_preco}'