#MENU E EXCEPT
#IMPORTAR MODELS

from models import *

def gerenciar_livros():
    print("\n===== Gerenciamento de livros")
    print("1 - Cadastrar livro"
          "\n2 - Buscar livros pelo codigo"
          "\n3 - Listar todos livros"
          "\n0 - Sair")

def gerenciar_emprestimos():
    print("\n===== Gereciamento de emprestimos")
    print("1 - Realizar emprestimo"
          "\n2 - Listar todos emprestimos"
          "\n3 - Buscar emprestimo pelo codigo"
          "\n0 - Sair")

def menu():
    while True:
        print("\n====== BIBLIOTECA =====")
        print("1 - Gerenciar Livros"
              "\n2 - Gerenciar Emprestimos"
              "\n0 - Sair")

        try:
            op = int(input("Digite uma opção: "))

            if op == 1:
                while True:
                    gerenciar_livros()

                    op1 =  int(input("Digite a opçãO: "))

                    if op1 == 1:
                        cadastrar_livro()
                    elif op1 == 2:
                        codigo_livro = input("Digite o codigo do livro: ")
                        buscar_livro_pelo_codigo(codigo_livro)
                    elif op1 == 3:
                        listar_todos_livros()
                    elif op1 == 0:
                        print("\nRetornando ao menu principal")
                        break
            elif op == 2:
                while True:
                    gerenciar_emprestimos()

                    op2 = int(input("Digite a opção: "))

                    if op2 == 1:
                        realizar_emprestimo()
                    elif op2 == 2:
                        listar_todos_emprestimos()
                    elif op2 == 3:
                        codigo_emprestimo = input("Digite o codigo de emprestimo: ")
                        buscar_emprestimo_pelo_codigo(codigo_emprestimo)
                    elif op2 == 0:
                        print("\nRetornando ao menu principal")
                        break
        except Exception as e:
            print(f"Error:{e}")

menu()