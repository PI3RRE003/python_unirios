from model import *

def gerenciar_produtos():
    print(f"\n{'='*10} GERENCIAR PRODUTOS {'='*10}")
    print("1 - Cadastrar Produto"
          "\n2 - Listar Produtos"
          "\n3 - Buscar Produto por Codigo"
          "\n4 - Atualizar Estoque"
          "\n5 - Remover Produto"
          "\n0 - Retornar ao menu principal")


def registrar_vendas():
    print(f"\n{'=' * 10} REGISTRAR VENDAS {'=' * 10}")
    print("1 - Registrar Venda"
          "\n2 - Listar Vendas"
          "\n3 - Buscar Venda pelo codigo"
          "\n4 - Alterar Venda"
          "\n5 - Remover Venda"
          "\n0 - Sair")


def menu():
    print(f"\n{'='*10} CARREGANDO SISTEMA {'='*10}")
    produtos_carregados = carregar_dados_produtos()
    vendas_carregadas = carregar_dados_vendas()
    print(f"PRODUTOS CARREGADOS:{len(produtos_carregados)}")
    print(f"VENDAS CARREGADAS:{len(vendas_carregadas)}")
    while True:
        print(f"\n{'='*10} CONTROLE DE ESTOQUE {'='*10}")
        print("1 - Gerenciar Produtos"
              "\n2 - Registrar Venda"
              "\n0 - Sair")

        op = int(input("Digite a opção: "))

        if op == 1:
            while True:
                gerenciar_produtos()
                op1 = int(input("Digite a opção: "))

                if op1 == 1:
                    cadastrar_produto()
                elif op1 == 2:
                    listar_produtos()
                elif op1 == 3:
                    codigo = input("Digite o codigo do produto: ")
                    buscar_por_codigo(codigo)
                elif op1 == 4:
                    codigo = input("Digite o codigo do produto: ")
                    atualizar_estoque(codigo)
                elif op1 == 5:
                    codigo = input("Digite o codigo do produto: ")
                    remover_produto(codigo)
                elif op1 == 0:
                    print("\nRetornando ao menu principal...")
                    break
        elif op == 2:
            while True:
                registrar_vendas()

                op2 = int(input("Digite a opção:"))

                if op2 == 1:
                    codigo = input("Digite o codigo do produto que deseja realizar a venda: ")
                    registrar_venda(codigo)
                elif op2 == 2:
                    listar_vendas()
                elif op2 == 3:
                    codigo = input("Digite o codigo do produto que deseja realizar a venda: ")
                    alterar_venda(codigo)
                elif op2 == 0:
                    print("\nRetornando ao menu principal...")
                    break

        elif op == 0:
            print("Finalizando o programa....")
            break


menu()