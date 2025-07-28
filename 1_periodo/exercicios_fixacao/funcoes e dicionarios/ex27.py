aluno = {
    'nome':'Vitor',
    'idade': 19,
}

aluno.update({
    'idade' : 20
})

for chave, valor in aluno.items():
    print(chave,':',valor)