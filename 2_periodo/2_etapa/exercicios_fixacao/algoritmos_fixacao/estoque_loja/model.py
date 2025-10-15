import json

produtos = []
PRODUTOS = 'produtos.json'

def salvar_dados_produtos(produtos):
    with open(PRODUTOS, 'w', encoding='utf-8') as arquivo:
        json.dump(produtos, arquivo, indent=4)

def carregar_dados_produtos():
    try:
        with open(PRODUTOS, 'r', encoding='utf-8') as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        print("\nArquivo não encontrado no sistema, iniciando uma lista vazia")
        return []

vendas = []
VENDAS = 'vendas.json'

def salvar_dados_vendas(vendas):
    with open(VENDAS, 'w', encoding='utf-8') as arquivo:
        json.dump(vendas, arquivo, indent=4)

def carregar_dados_vendas():
    try:
        with open(VENDAS, 'r', encoding='utf-8') as arquivo:
            return  json.load(arquivo)
    except FileNotFoundError:
        print("\nArquivo não encontrado no sistema, iniciando uma lista vazia")
        return []


def cadastrar_produto():

    print(f"\n{'=' * 10} CADASTRANDO PRODUTO {'=' * 10}")

    codigo = "00" + str(gerar_codigo())
    nome = input("Digite o nome do produto: ")

    try:
        preco = float(input("Digite o preço do produto: "))
        qtd_estoque = float(input("Digite a quantidade em estoque do produto: "))
    except ValueError:
        print("Error: Digite apenas numeros")

    produto = {
        'codigo' : codigo,
        'nome' : nome,
        'preco' : preco,
        'estoque' : qtd_estoque
    }
    produtos = carregar_dados_produtos()
    produtos.append(produto)
    salvar_dados_produtos(produtos)
    print("\nPRODUTO CADASTRADO COM SUCESSO !!")
    print(f"\nCodigo:{produto['codigo']} - Nome:{produto['nome']} - Preço:{produto['preco']} - Estoque:{produto['estoque']}")


def gerar_codigo():
    produtos = carregar_dados_produtos()
    if not produtos:
        codigo = 1
    else:
        codigo = len(produtos)+1
    return codigo

def listar_produtos():
    produtos = carregar_dados_produtos()
    print(f"\n{'=' * 10} LISTANDO PRODUTOS {'=' * 10}")
    for produto in produtos:
        print(f"\nCodigo:{produto['codigo']} - Nome:{produto['nome']} - Preço:{produto['preco']} - Estoque:{produto['estoque']}")

def buscar_por_codigo(codigo):
    produtos = carregar_dados_produtos()
    print(f"\n{'=' * 10} BUSCANDO PRODUTO POR CODIGO {'=' * 10}")
    for produto in produtos:
        if produto['codigo'] == codigo:
            print(f"\nCodigo:{produto['codigo']} - Nome:{produto['nome']} - Preço:{produto['preco']} - Estoque:{produto['estoque']}")

def atualizar_estoque(codigo):
    produtos = carregar_dados_produtos()
    print(f"\n{'=' * 10} ATUALIZANDO ESTOQUE DO PRODUTO {'=' * 10}")
    for produto in produtos:
        if produto['codigo'] == codigo:
            print(f"\nCodigo:{produto['codigo']} - Nome:{produto['nome']} - Preço:{produto['preco']} - Estoque:{produto['estoque']}")

            try:
                op = int(input("\nO que deseja fazer?\n1 - Adicionar\n2 - Remover\n0 - Retornar\nDigite a opção: "))
            except ValueError:
                print("Error: Digite apenas numeros")

            if op == 1:
                qtd = float(input("Digite a quantidade que deseja adicionar ao estoque: "))
                if qtd > 0:
                    produto['estoque'] += qtd
                    salvar_dados_produtos(produtos)
                else:
                    print("Quantidade não pode ser menor que zero")
            elif op == 2:
                qtd = float(input("Digite a quantidade que deseja remover do estoque: "))
                if qtd <= 0:
                    print("Quantidade não pode ser menor que zero")
                elif qtd > produto['estoque']:
                    print("Error: Estoque não pode ser negativo")
                else:
                    produto['estoque'] -= qtd
                    print("\nEstoque atualizado com sucesso")
                    print(f"\nNome:{produto['nome']} - Estoque:{produto['estoque']}")
                    salvar_dados_produtos(produtos)
            elif op == 0:
                print("Retornando ao menu...")
                return

def remover_produto(codigo):
    produtos = carregar_dados_produtos()
    for produto in produtos:
        if produto['codigo'] == codigo:
            print(f"\nCodigo:{produto['codigo']} - Nome:{produto['nome']} - Preço:{produto['preco']} - Estoque:{produto['estoque']}")
            produtos.remove(produto)
            salvar_dados_produtos(produtos)
            print("Produto removido com sucesso!")


'''------------------- VENDAS -------------------'''

def registrar_venda(codigo):
    print(f"\n{'=' * 10} REGISTRANDO VENDA DO PRODUTO {'=' * 10}")
    produtos = carregar_dados_produtos()
    for produto in produtos:
        if produto['codigo'] == codigo:
            print(f"\nCodigo:{produto['codigo']} - Nome:{produto['nome']} - Preço:{produto['preco']} - Estoque:{produto['estoque']}")

            try:
                qtd_venda = int(input("Digite a quantidade vendida: "))
            except ValueError:
                print("Error: Digite apenas numeros")

            if qtd_venda <= 0:
                print("Error: quantidade de venda não pode ser menor ou igual a zero")
                return
            elif qtd_venda > produto['estoque']:
                print("Error: Não pode vender quantidade maior que a do estoque")
                return
            else:
                codigo_da_venda = "00" + str(codigo_venda())
                qtd_venda -= produto['estoque']
                qtd_venda *= produto['preco']
                venda ={
                    'codigo' : codigo_da_venda,
                    'nome' : produto['nome'],
                    'preco' : qtd_venda,
                    'quantidade' : qtd_venda
                }
                vendas = carregar_dados_vendas()
                vendas.append(venda)
                salvar_dados_vendas(vendas)
                print(f"\nVENDA REALIZADA COM SUCESSO !!!")
                print(f"\n{venda['codigo']} -  Nome:{venda['nome']} - Preço total:{venda['preco']} - Quantidade vendida:{qtd_venda}")


def codigo_venda():
    if not vendas:
        codigo = 1
    else:
        codigo = len(vendas)+1
    return  codigo

def listar_vendas():
    vendas_carregadas = carregar_dados_vendas()
    for venda in vendas_carregadas:
        print(f"\n{venda['codigo']} -  Nome:{venda['nome']} - Preço total:{venda['preco']} - Quantidade vendida:{venda['quantidade']}")

def alterar_venda(codigo):
    vendas = listar_vendas()
    if codigo == vendas['codigo']:
        print("PASSOU")