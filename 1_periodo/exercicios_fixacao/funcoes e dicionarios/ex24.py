nome_e_idade =[
  {"nome": "Ana", "idade": 20},
  {"nome": "Carlos", "idade": 21},
  {"nome": "João", "idade": 20}
]

def agrupa_por_idade(lista_de_pessoas):
    agrupado = {}
    for pessoa in lista_de_pessoas:
        idade = pessoa['idade']
        nome = pessoa['nome']
        
        if idade in agrupado:
            agrupado[idade].append(nome)
        else:
            agrupado[idade] = [nome]
    return agrupado

resultado = agrupa_por_idade(nome_e_idade)
print(resultado)