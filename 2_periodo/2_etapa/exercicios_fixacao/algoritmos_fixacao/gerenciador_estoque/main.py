from models import *

def menu():
    print("\n===== GERENCIAMENTO DE ESTOQUE =====")
    print("1 - Adicionar Novo Produto"
          "\n2 - Registrar Entrada de Estoque"
          "\n3 - Registrar Saida do Estoque"
          "\n4 - Listar todos os Produtos"
          "\n5 - Buscar Produto "
          "\n0 - Sair")


def main():
    while True:
        try:
            menu()

            op = int(input("Digite uma opção: "))

            if op == 1:
                adicionar_produto()
            elif op == 2:
                codigo_produto = input("Digite o codigo do produto que deseja registrar a entrada: ")
                registrar_entrada(codigo_produto)
            elif op == 3:
                codigo_produto = input("Digite o codigo do produto que deseja registrar a saida: ")
                registrar_saida(codigo_produto)
            elif op == 4:
                listar_todos_produtos()
            elif op == 5:
                codigo_produto = input("Digite o codigo do produto que deseja registrar a saida: ")
                buscar_produto(codigo_produto)
            elif op == 0:
                print("\nEncerrando o programa....")
                break
        except ValueError:
            print("Error: Digite apenas Numeros")
        except Exception as e:
            print(f"Error:{e}")

main()