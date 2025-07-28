produtos = {
    "arroz": 10, 
    "feijão": 8, 
    "macarrão": 5
}

for chave, valor in produtos.items():
    print(chave,':',valor)

'''Minha solução'''
# arroz = produtos["arroz"]
# feijao = produtos["feijão"]
# macarrao = produtos["macarrão"]

# soma = arroz + feijao + macarrao

#GPT
soma = sum(produtos.values())
print(f'A soma do arroz, feijao e macarrao deu total de:{soma}')