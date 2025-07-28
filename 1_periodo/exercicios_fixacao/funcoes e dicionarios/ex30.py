pessoa = {
    'nome':'Vitor',
    'idade': 22,
    'cidade':'Canapi'
}

def informacoes_usuario(usuario):
    return f'"Nome: {usuario['nome']} | Idade: {usuario['idade']} | Cidade: {usuario['cidade']}"'
    

print(informacoes_usuario(pessoa))