import json

print("========== INICIANDO PROCESSO DE SALVAR =========")
lista_de_contatos = [
    {'nome': 'Vitor Pierre', 'telefone' : '82982374664'}
]

nome_do_arquivo = "contatos.json"

with open(nome_do_arquivo, 'w', encoding='utf-8') as arquivo:
    json.dump(lista_de_contatos, arquivo, indent=4, ensure_ascii=False)

print("Dados salvos com sucesso")
print("\n=================================================\n")

print("========== INICIANDO PROCESSO DE CARREGAR =========")
dados_carregados = []

try:
    with open(nome_do_arquivo,'r', encoding='utf-8') as arquivo:
        dados_carregados = json.load(arquivo)
    print("Dados carregados com sucesso")
except FileNotFoundError:
    print(f"O arquivo:{nome_do_arquivo} não foi encontrado")

print("\n========= DADOS CARREGADOS =========")
for dado in dados_carregados:
    print(f'Nome: {dado['nome']} - Telefone:{dado['telefone']}')