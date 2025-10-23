estoque = []

def adicionar_produto():
    print("\n===== ADICIONANDO PRODUTO ======")
    try:
        codigo_produto = "00" + str(gerar_codigo())
        print(f"Codigo do Produto:{codigo_produto}")

        nome_produto =  input("Digite o nome do produto: ")

        quantidade =  float(input("Digite a quantidade do produto: "))

        produto = {
            'codigo' : codigo_produto,
            'nome' : nome_produto,
            'quantidade' : quantidade
        }
        estoque.append(produto)
        print(f"\nPRODUTO ADICIONADO COM SUCESSO !!!"
              f"\nCodigo:{produto['codigo']}"
              f"\nNome:{produto['nome']}"
              f"\nQuantidade:{produto['quantidade']}")

    except Exception as e:
        print(f"Error:{e}")

def gerar_codigo():
    if len(estoque) == 0:
        codigo_produto = 1
    else:
        codigo_produto = len(estoque)+1
    return codigo_produto

def normalizar_texto(texto):
    return  texto.lower().replace('P','')

def registrar_entrada(codigo):
    print("\n====== REGISTRANDO ENTRADA DO PRODUTO ======")
    try:
        if buscar_produto(codigo):
            op = int(input("\nDigite a Opção Desejada"
                           "\n1 - Registrar entrada"
                           "\n0 - Retornar ao Menu"
                           "\nOpção:"))

            if op == 1:
                try:
                    entrada = float(input("\nDigite a quantidade de entrada do produto: "))
                    if entrada <= 0:
                        print("Error: entrada deve ser maior que zero")
                    else:
                        codigo['quantidade'] += entrada
                        print(f"PRODUTO ATUALIZADO COM SUCESSO !!!"
                              f"\nNome:{codigo['nome']}"
                              f"\nQuantidade:{codigo['quantidade']}")
                except ValueError:
                    print("Digite apenas numeros")
                    return
            elif op == 0:
                print("\nRetornando ao Menu")
                return
    except Exception as e:
        print(f"Error:{e}")

def registrar_saida(codigo):
    print("\n====== REGISTRANDO SAIDA DO PRODUTO ======")
    try:
        if buscar_produto(codigo):
                op = int(input("\nDigite a Opção Desejada"
                               "\n1 - Registrar Saida"
                               "\n0 - Retornar ao Menu"
                               "\nOpção:"))

                if op == 1:
                    try:
                        saida = float(input("\nDigite a quantidade de saida do produto: "))
                        if saida <= codigo['quantidade']:
                            codigo['quantidade'] -= saida
                            print(f"PRODUTO ATUALIZADO COM SUCESSO !!!"
                                  f"\nNome:{codigo['nome']}"
                                  f"\nQuantidade:{codigo['quantidade']}")
                        else:
                            print("Error: saida deve ser igual ao estoque ou menor")
                    except ValueError:
                        print("Digite apenas numeros")
                        return
                elif op == 0:
                    print("\nRetornando ao Menu")
                    return
    except Exception as e:
        print(f"Error:{e}")

def listar_todos_produtos():
    print("===== LISTANDO TODOS OS PRODUTOS =====")
    try:
        for produto in estoque:
            if not produto:
                print("\nLista de produtos vazia")
            else:
                print(f"\nCodigo:{produto['codigo']}"
                      f"\nNome:{produto['nome']}"
                      f"\nQuantidade:{produto['quantidade']}")
    except Exception as e:
        print(f"Error:{e}")


def buscar_produto(codigo):
    try:
        for produto in estoque:
            if produto['codigo'] == codigo:
                print(f"\nCodigo:{produto['codigo']}"
                      f"\nNome:{produto['nome']}"
                      f"\nQuantidade:{produto['quantidade']}")
            else:
                print("\nProduto não encontrado, retornando ao menu")
                return
    except Exception as e:
        print(f"Error:{e}")