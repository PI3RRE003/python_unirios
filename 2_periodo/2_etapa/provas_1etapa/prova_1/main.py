from models import  *

def menu_livros():
    print("\n====== GERENCIAR LIVROS =====")
    print("1 - Cadastrar Livro"
          "\n2 - Buscar Livro pelo Codigo"
          "\n3 - Listar Todos os Livros Cadastrados"
          "\n4 - Controlar quantidade de exemplar"
          "\n0 -  sair")

def menu_emprestimos():
    print("\n====== GERENCIAR EMPRESTIMOS =====")
    print("1 - Realizar emprestimo"
          "\n2 - Listar todos emprestimos"
          "\n3 - Buscar emprestimo pelo codigo"
          "\n0 - sair")
def menu():
    print("\n===== CONTROLE BIBLIOTECA =====")
    print("1 - Gerenciar Livros"
          "\n2 - Gerenciar emprestimos"
          "\n0 - Sair")
def main():
    while True:
        menu()
        try:
            op = int(input("Digite uma opção: "))
            if op == 1:
                while True:
                    menu_livros()

                    op1 = int(input("Digite a opção: "))
                    if op1 == 1:
                        cadastrar_livro()
                    elif op1 == 2:
                        codigo = input("Digite o codigo do livro que deseja buscar: ")
                        buscar_livro_pelo_codigo(codigo)
                    elif op1 == 3:
                        listar_todos_livros_cadastrados()
                    elif op1 == 4:
                        codigo= input("Digite o codigo do livro que deseja buscar: ")
                        controlar_quantidade_exemplar(codigo)
                    elif op1 == 0:
                        print("Retornando ao menu principal..")
                        break
                    else:
                        print("Digite de 0 a 4")
            elif op == 2:
                while True:
                    menu_emprestimos()

                    op2 = int(input("Digite a opção: "))
                    if op2 == 1:
                        codigo = input("Digite o codigo do livro que deseja realizar o emprestimo: ")
                        realizar_emprestimo(codigo)
                    elif op2 == 2:
                        listar_todos_emprestimos()
                    elif op2 == 3:
                        codigo = input("Digite o codigo do livro que deseja buscar pelo emprestimo: ")
                        buscar_emprestimo_pelo_codigo(codigo)
                    elif op2 == 0:
                        print("Retornando ao menu principal...")
                        break
                    else:
                        print("Digite de 0 a 3")
            else:
                print("Digite de 0 a 2")
        except ValueError:
            print("Digite apenas numeros")
        except Exception as e:
            print(f"Error:{e}")

main()