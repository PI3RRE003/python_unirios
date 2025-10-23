from  models import *
def menu():
    print("\n===== GERENCIADOR DE LIVROS =====")
    print("1 - Adicionar livro"
          "\n2 - Listar Livros Lidos"
          "\n3 - Listar Livros Não Lidos"
          "\n4 - Marcar como lido"
          "\n5 - Buscar Livro"
          "\n6 - Remover Livro"
          "\n7 - Listar por ano"
          "\n0 - Sair")

def main():
    while True:
        try:
            menu()
            op = int(input("Digite uma opção: "))

            if op == 1:
                adicionar_livro()
            elif op == 2:
                listar_livros_lidos()
            elif op == 3:
                listar_livros_nao_lidos()
            elif op == 4:
                marcar_como_lido()
            elif op == 5:
                termo_busca = input("Digite o titulo ou nome do autor: ")
                buscar_livro(termo_busca)
            elif op == 6:
                remover_livro()
            elif op == 7:
                ano = int(input("Digite o ano que deseja listar os livros"))
                listar_por_ano(ano)
            elif op == 0:
                print("Encerrando o programa....")
                break
        except ValueError:
            print("Error: Digite apenas numeros de 0 a 5")
        except Exception as e:
            print(f"Error{e}")
            
main()