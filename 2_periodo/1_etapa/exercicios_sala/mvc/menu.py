from model import *

def menu_principal():
    print("\n========== MENU PRINCIPAL =========")
    print("1 - Cliente\
          \n2 - Produto\
          \n3 - Venda\
          \n0 - Sair")
    
def menu_cliente():
    print("\n========== MENU CLIENTE ==========")
    print("1 - Cadastrar cliente\
          \n2 - Buscar Cliente\
          \n3 - Listar Clientes\
          \n4 - Atualizar Cliente\
          \n0 - Sair")

def menu_produto():
    print("\n========== MENU PRODUTO =========")
    print("1 - Cadastrar produto\
          \n2 - Buscar Produto\
          \n3 - Listar Produtos\
          \n4 - Controlar Estoque\
          \n0 - Sair")
    
def menu_venda():
    print("\n========== MENU VENDA =========")
    print("1 - Registrar Venda\
          \n2 - Buscar Vendas\
          \n3 - Listar Vendas\
          \n0 - Sair")

def main():
    while True:
        menu_principal()
        op = int(input("Digite a opção: "))

        if op == 1:
            while True:
                menu_cliente()
                op1 = int(input("Digite uma opção: "))

                if op1 == 1:
                    cadastrar_cliente()
                elif op1 == 2:
                    cod = input("Informe o codigo do cliente: ")
                    buscar_cliente(cod)
                elif op1 == 3:
                    listar_clientes()
                elif op1 == 4:
                    cod = input("Informe o codigo do cliente que deseja atualizar:")
                    atualizar_cliente(cod)
                elif op1 == 0:
                    print("Saindo do Menu de clientes")
                    break
                else:
                    print("ERRO: DIGITE UM NUMERO DE 0 A 4")

        elif op == 2:
            while True:
                menu_produto()
                op2 = int(input("Digite uma opção: "))

                if op2 == 1:
                    cadastrar_produto()
                elif op2 == 2:
                    cod = input("Informe o codigo do produto: ")
                    buscar_produto(cod)
                elif op2 == 3:
                    listar_produtos()
                elif op2 == 4:
                    controlar_estoque()
                elif op2 == 0:
                    print("saindo do menu do produto: ")
                    break
                else:
                    print("ERRO: DIGITE UM NUMERO DE 0 A 4")

        elif op == 3:
            while True:
                menu_venda()
                op3 = int(input("Digite uma opção: "))

                if op3 == 1:
                    cod = input("Informe o codigo do produto: ")
                    registrar_venda(cod)
                elif op3 == 2:
                    buscar_vendas()
                elif op3 == 3:
                    listar_vendas()
                elif op3 == 0:
                    print("saindo do menu de vendas")
                    break
                else:
                    print("ERRO: DIGITE UM NUMERO DE 0 A 3")

        elif op == 0:
            print("Encerrando o programa....")
            break
        else:
            print("ERRO: DIGITE 0 PARA SAIR")

main()