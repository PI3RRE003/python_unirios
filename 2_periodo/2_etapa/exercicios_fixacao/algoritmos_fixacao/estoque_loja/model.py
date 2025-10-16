import json

produtos = []
PRODUTOS = 'produtos.json'

def salvar_dados_produtos(produtos):
    with open(PRODUTOS, 'w', encoding='utf-8') as arquivo:
        json.dump(produtos, arquivo, ensure_ascii=False ,indent=4)

def carregar_dados_produtos():
    try:
        with open(PRODUTOS, 'r', encoding='utf-8') as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return []

vendas = []
VENDAS = 'vendas.json'

def salvar_dados_vendas(vendas):
    with open(VENDAS, 'w', encoding='utf-8') as arquivo:
        json.dump(vendas, arquivo, ensure_ascii=False ,indent=4)

def carregar_dados_vendas():
    try:
        with open(VENDAS, 'r', encoding='utf-8') as arquivo:
            return  json.load(arquivo)
    except FileNotFoundError:
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
        return

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
                continue

            if op == 1:

                try:
                    qtd = float(input("Digite a quantidade que deseja adicionar ao estoque: "))
                except ValueError:
                    print("\nError: Digite apenas numeros")
                    continue

                if qtd > 0:
                    produto['estoque'] += qtd
                    salvar_dados_produtos(produtos)
                else:
                    print("Quantidade não pode ser menor que zero")
            elif op == 2:

                try:
                    qtd = float(input("Digite a quantidade que deseja remover do estoque: "))
                except ValueError:
                    print("\nError: Digite apenas numeros")
                    continue

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
                continue

            if qtd_venda <= 0:
                print("Error: quantidade de venda não pode ser menor ou igual a zero")
                return
            elif qtd_venda > produto['estoque']:
                print("Error: Não pode vender quantidade maior que a do estoque")
                return
            else:
                carregar_dados_vendas()
                codigo_da_venda = "00" + str(codigo_venda())
                preco = produto['preco']
                qtd_vendida = qtd_venda
                valor_total = preco * qtd_venda
                venda ={
                    'codigo' : codigo_da_venda,
                    'nome' : produto['nome'],
                    'preco' : valor_total,
                    'quantidade' : qtd_vendida
                }
                vendas = carregar_dados_vendas()
                vendas.append(venda)
                salvar_dados_vendas(vendas)
                print(f"\nVENDA REALIZADA COM SUCESSO !!!")
                print(f"\n{venda['codigo']} -  Nome:{venda['nome']} - Preço total:{venda['preco']} - Quantidade vendida:{qtd_venda}")


def codigo_venda():
    vendas = carregar_dados_vendas()
    if not vendas:
        codigo = 1
    else:
        codigo = len(vendas)+1
    return  codigo

def listar_vendas():
    print(f"\n{'=' * 10} LISTANDO VENDAS {'=' * 10}")
    vendas_carregadas = carregar_dados_vendas()
    for venda in vendas_carregadas:
        print(f"\n{venda['codigo']} -  Nome:{venda['nome']} - Preço total:{venda['preco']} - Quantidade vendida:{venda['quantidade']}")

def buscar_venda_pelo_codigo(codigo):
    print(f"\n{'=' * 10} BUSCANDO VENDAS PELO CODIGO {'=' * 10}")
    vendas = carregar_dados_vendas()
    for venda in vendas:
        if venda['codigo'] == codigo:
            print(f"\n{venda['codigo']} -  Nome:{venda['nome']} - Preço total:{venda['preco']} - Quantidade vendida:{venda['quantidade']}")

def alterar_venda_pelo_codigo(codigo):
    print(f"\n{'=' * 10} ALTERANDO VENDA PELO CODIGO {'=' * 10}")
    vendas = carregar_dados_vendas()
    for venda in vendas:
        if venda['codigo'] == codigo:
            print(f"\nPRODUTO ENCONTRADO!\n{venda['codigo']} -  Nome:{venda['nome']} - Preço total:{venda['preco']} - Quantidade vendida:{venda['quantidade']}\n")

            op = int(input("O que deseja alterar?\n1 - Preço\n2 - Quantidade\n0 - Sair\nDigite a opção:"))

            if op == 1:
                print("\nVocê escolheu a opção de alterar preço\n")

                try:
                    novo_preco = float(input("Digite o novo preço: "))
                except ValueError:
                    print("Error: Digite apenas numeros")
                    continue

                venda['preco'] = novo_preco * venda['quantidade']
                print(f"\nCodigo:{venda['codigo']} -  Nome:{venda['nome']} - Preço total:{venda['preco']} - Quantidade vendida:{venda['quantidade']}\n")
                salvar_dados_vendas(vendas)

            elif op == 2:
                print("\nVocê escolheu a opção de alterar estoque\n")

                try:
                    nova_qtd = int(input("Digite a nova quantidade: "))
                except ValueError:
                    print("Error: Digite apenas numeros")
                    continue

                venda['quantidade'] = nova_qtd
                preco_total = venda['preco'] * nova_qtd
                venda['preco'] = preco_total
                print(f"\nCodigo:{venda['codigo']} -  Nome:{venda['nome']} - Preço total:{venda['preco']} - Quantidade vendida:{venda['quantidade']}\n")
                salvar_dados_vendas(vendas)
            elif op == 0:
                print("\nRetornando ao menu principal...")
                return

def remover_venda(codigo):
    vendas = carregar_dados_vendas()
    for venda in vendas:
        if venda['codigo'] == codigo:
            vendas.remove(venda)
            salvar_dados_vendas(vendas)
            print(f"\nPRODUTO REMOVIDO COM SUCESSO !!!\nCodigo:{venda['codigo']} -  Nome:{venda['nome']} - Preço total:{venda['preco']} - Quantidade vendida:{venda['quantidade']}\n")
