estoque = {
    'Arroz': 10,
    'Feijão': 5,
    'Macarrão': 14
    }

def atualiza_estoque(estoque, produto, quantidade):
    for produto in estoque:
        estoque[produto] += quantidade
        return f'Produto já existe. Estoque atualizado: {estoque[produto]}'
    else:
        estoque[produto] = quantidade
        return f'Novo produto adicionado: {produto}, quantidade: {quantidade}'
    
print(atualiza_estoque(estoque, 'Suco', 10))
print(atualiza_estoque(estoque, 'Arroz', 5))

print("\nEstoque final:")
for produto, qtd in estoque.items():
    print(f'{produto}: {qtd}')