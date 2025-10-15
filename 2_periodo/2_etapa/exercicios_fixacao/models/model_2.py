produtos = []

def adicionar_produto():
    print("\n========= ADICIONANDO PRODUTO ========")
    codigo = "00" + str(gerar_codigo())

    try:
        nome = input("Digite o nome do produto: ")
        if verifica_nome(nome): return

        preco = float(input("Digite o preço do produto: "))
        quantidade = float(input("Digite a quantidade inicial do produto: "))
    except ValueError:
        print("Error: Verifique os campos")
        return

    produto = {
        'codigo' : codigo,
        'nome' : nome,
        'preco' : preco,
        'quantidade' : quantidade
    }
    produtos.append(produto)
    print("\nPRODUTO CADASTRADO COM SUCESSO !!")
    print(f"Codigo:{produto['codigo']} - Nome: {produto['nome']} - Preço R$:{produto['preco']} - Quantidade: {produto['quantidade']}")

def gerar_codigo():
    if len(produtos) == 0:
        codigo = 1
    else:
        codigo = len(produtos)+1
    return  codigo

def verifica_nome(nome):
    if len(nome) == 0:
        print("Error: Nome não pode ser vazio !!!")
        return True
    return False

def verifica_lista_vazia():
    if len(produtos) == 0:
        print("Lista de produtos vazia")
        op = input("Deseja adiconar? (S/N): ")
        if op.lower() == 's':
            print("Redirecionando para adicionar um produto")
            adicionar_produto()
            return True
        elif op.lower() == 'n':
            print("Retornando ao menu principal")
            return  False
        else:
            print("Digite apenas (S/N)")
            return False
    return True


def listar_todos_produtos():
    prosseguir = verifica_lista_vazia()
    if prosseguir:
        print("\n========= LISTANDO TODOS OS PRODUTOS ========")
        for produto in produtos:
            print(f"Codigo:{produto['codigo']} - Nome: {produto['nome']} - Preço R$:{produto['preco']} - Quantidade: {produto['quantidade']}")


def atualizar_estoque():
    prosseguir = verifica_lista_vazia()
    if prosseguir:
        print("\n========= ATUALIZANDO ESTOQUE ==========")
        try:
            codigo_produto = input("Digite o codigo do produto: ")
        except ValueError:
            print("\nError: Codigo não encontrado")

        for produto in produtos:
            if produto['codigo'] == codigo_produto:
                print(f"\nPRODUTO ENCONTRADO:\nCodigo:{produto['codigo']} - Nome: {produto['nome']} - Preço R$:{produto['preco']} - Quantidade: {produto['quantidade']}")
                op = input("\nDigite o nome do que deseja alterar: ")

                if op.lower() == 'nome':
                    novo_nome = input("\nDigite o novo nome: ")
                    produto['nome'] = novo_nome
                elif op.lower() == 'preco':
                    novo_preco = float(input("Digite o novo preço: "))
                    produto['preco'] = novo_preco
                elif op.lower() == 'quantidade':
                    nova_quantidade = float(input("Digite o novo preço: "))
                    produto['quantidade'] = nova_quantidade
                else:
                    print("Error: Digite corretamente")
            else:
                print("Erro: Produto não encontrado")


def buscar_produto_pelo_nome():
    prosseguir = verifica_lista_vazia()
    if prosseguir:
        print("\n=========== BUSCANDO PELO PRODUTO ==========")
        try:
            nome = input("Digite o nome do produto que deseja atualizar: ")
        except ValueError:
            print("Error: nome não encontrado")

        for produto in produtos:
            if produto['nome'] == nome:
                print(f"\nPRODUTO ENCONTRADO:\nCodigo:{produto['codigo']} - Nome: {produto['nome']} - Preço R$:{produto['preco']} - Quantidade: {produto['quantidade']}")
            else:
                print("Pessoa não encontrada")

def remover_produto():
    prosseguir = verifica_lista_vazia()
    if prosseguir:
        print("\n========== REMOVENDO PRODUTO =========")
        for produto in produtos:
            print(f"Codigo:{produto['codigo']} - Nome: {produto['nome']} - Preço R$:{produto['preco']} - Quantidade: {produto['quantidade']}")

        codigo = input("\nDigite o codigo do produto que deseja remover: ")
        for produto in produtos:
            if produto['codigo'] == codigo:
                print(f"\nPRODUTO ENCONTRADO:\nCodigo:{produto['codigo']} - Nome: {produto['nome']} - Preço R$:{produto['preco']} - Quantidade: {produto['quantidade']}")

                op = input("Deseja remover? (S/N): ")
                if op.lower() == 's':
                    produtos.remove(produto)
                    print(f"Produto:{produto['nome']} removido com sucesso")
                elif op.lower() == 'n':
                    print("\nRetornando ao menu..")
                    return
            else:
                print("Error: produto não encontrado.")

