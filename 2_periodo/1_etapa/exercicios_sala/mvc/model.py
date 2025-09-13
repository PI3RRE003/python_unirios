''' PRODUTO: codigo, nome, e qtd '''

produtos = []

def cadastrar_produto():
    print("\n======== CADASTRAR PRODUTOS =========")
    cod = "00" + str(gerar_codigo())
    nome = input("Digite o nome do produto: ")
    qtd = int(input("Digite a quantidade em estoque: "))
    produto = [cod, nome, qtd]
    produtos.append(produto)
    print(f"Produto: {nome} cadastrado com sucesso")

def gerar_codigo():
    if len(produtos) == 0:
        cod = 1
    else:
        cod = len(produtos)+1
    return cod

def buscar_produto(cod):
    print("\n========== BUSCAR PRODUTO ==========")
    for produto in produtos:
        if produto[0] == cod:
            print(f"Produto devidamente cadastrado\nCodigo:{produto[0]} - Produto:{produto[1]} ")
            return True
    
    print("Produto não encotrado cadastre-o")
    return False
    

def listar_produtos():
    print("\n======== LISTANDO PRODUTOS ==========")
    for produto in produtos:
        print(f"Codigo: {produto[0]} - Nome: {produto[1]} - Estoque: {produto[2]}")

def controlar_estoque():
    pass

'''VENDAS'''

vendas = []

def registrar_venda(cod):
    print("======== REGISTRAR VENDA ===========")
    if buscar_produto(cod):
        for produto in produtos:
            if produto[0] == cod:
                if produto[2] == 0:
                    print("Erro produto sem estoque")
                else:
                    print(f"Quantidade em estoque:{produto[2]}")
                    qtd = int(input("Quantas unidades serão vendidas: "))
                    if qtd > produto[2]:
                        print("Erro: Quantidade impossivel de realizar venda")
                    else:
                        produto[2] -= qtd
                        cod_venda = "V0"+str(len(vendas)+1)
                        venda = [cod_venda, produto[0], produto[1], produto[2]]
                        vendas.append(venda)
                        print("Venda registrada com sucesso")
                        print("========== NOTA FISCAL =========")
                        print(f"Codigo venda: {cod_venda}")
                        print(f"Produto:{produto[0]} - Nome:{produto[1]} Quantidade:{qtd}")
                        print("================================")
    else:
        print("Erro Impossivel realizar venda")

def listar_vendas():
    for venda in vendas:
        print(f"\nCodigo venda: {venda[0]}")
        print(f"Produto:{venda[0]} - Nome:{venda[1]} - Quantidade:{venda[2]}")

def buscar_vendas(cod):
    for venda in vendas:
        if venda[0] == cod:
            print(f"\nCodigo venda: {venda[0]}")
            print(f"Produto:{venda[0]} - Nome:{venda[1]} - Quantidade:{venda[2]}")
            return True
    
    print("Codigo de venda não encontrado")
    return False

'''CLIENTES'''

clientes = []

def cadastrar_cliente():
    print("\n========= CADASTRO DE CLIENTE ==========")
    cod = "00" + str(gerar_codigo())
    nome = input("Digite o Nome do Cliente: ")
    cpf = input("Digite o CPF do Cliente: ")
    cliente = [cod, nome, cpf]
    clientes.append(cliente)
    print(f"\nCliente:{cliente[1]} cadastrado com sucesso, Codigo:{cliente[0]}")

def buscar_cliente(cod):
    for cliente in clientes:
        if cliente[0] == cod:
            print("\nCliente Cadastrado:")
            print(f"Nome:{cliente[1]} - CPF:{cliente[2]}")
            return True
    
    print("Cliente não encontrado na base de dados")
    return False

def listar_clientes():
    for cliente in clientes:
        print(f"Codigo:{cliente[0]} - Nome:{cliente[1]} - CPF:{cliente[2]}")

def atualizar_cliente(cod):
    if buscar_cliente(cod):
        for cliente in clientes:
            if cliente[0] == cod:
                nome =input("Digite o novo nome do cliente: ")
                cliente[1] = nome
                print(f"Nome atualizado com sucesso:{nome}")
            else:
                print("ERRO")