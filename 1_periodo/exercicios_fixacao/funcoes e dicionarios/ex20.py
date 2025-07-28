aluno = {
    'nome':'Vitor',
    'sobrenome':'Pierre',
    'idade': 22,
    'curso':'"Sistemas de Informação"' 
}

def exibir_dados(aluno):
    dados = ''
    for chave, valor in aluno.items():
        dados += f'{chave}: {valor}\n'
    return dados

exibir_aluno = exibir_dados(aluno)
print(exibir_aluno)