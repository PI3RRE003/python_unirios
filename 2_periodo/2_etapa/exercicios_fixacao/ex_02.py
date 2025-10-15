from models.model_2 import *
def menu():
    while True:
        print("\n========= Gerenciador de estoque =========")
        print("1 - Adicionar Produto"
              "\n2 - Listar todos os produtos"
              "\n3 - Atualizar Estoque"
              "\n4 - Buscar produto por nome"
              "\n5 - Remover produto"
              "\n0 - Sair")

        op = int(input("Digite a opção: "))

        if op == 1:
            adicionar_produto()
        elif op == 2:
            listar_todos_produtos()
        elif op == 3:
            atualizar_estoque()
        elif op == 4:
            buscar_produto_pelo_nome()
        elif op == 5:
            remover_produto()
        elif op == 0:
            print("\nEncerrando o programa....")
            break


menu()
