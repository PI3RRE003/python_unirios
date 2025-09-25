from model.model_01 import *

def menu_livros():
    print("\n========== MENU LIVROS =========")
    print("1 - Registrar livros\
          \n2 - Buscar por ISBN\
          \n3 - Listar todos os livros\
          \n0 - Voltar para menu principal")
    print("============================================")

def menu_usuarios():
    print("\n========== MENU USUARIOS ==========")
    print("1 - Registrar Usuarios\
          \n2 - Buscar por codigo\
          \n3 - Listar todos usuarios\
          \n0 - Voltar para menu principal")
    print("============================================")
    
def menu_emprestimos():
    print("\n========== MENU EMPRESTIMOS ==========")
    print("1 - Realizar Emprestimo\
          \n2 - Listar todos Emprestimos\
          \n3 - Buscar Emprestimo por ISBN\
          \n0 - Voltar para menu principal")
    print("============================================")

def menu():
    while True:
        print("\n========== GERENCIADOR DE LIVROS ===========")
        print("1 - Menu Livros\
            \n2 - Menu Usuarios\
            \n3 - Menu Emprestimos\
            \n0 - Sair do programa")
        print("============================================")

        op = int(input("\nDigite a opção: "))
        
        if op == 1:
            while True:
                menu_livros()

                op1 = int(input("Digite a opção: "))

                if op1 == 1:
                    registrar_livros()
                elif op1 == 2:
                    isbn = input("Digite o ISBN: ")
                    buscar_por_isbn(isbn)
                elif op1 == 3:
                    listar_todos_livros()
                elif op1 == 0:
                    print("\nRetornando ao menu principal !!!")
                    break
        
        elif op == 2:
            while True:
                menu_usuarios()

                op2 = int(input("Digite a opção: "))

                if op2 == 1:
                    registrar_usuarios()
                elif op2 == 2:
                    codigo = input("Digite o codigo do usuario: ")
                    buscar_por_codigo(codigo)
                elif op2 == 3:
                    listar_todos_usuarios()
                elif op2 == 0:
                    print("\nRetornando ao menu principal !!!")
                    break
        
        elif op == 3:
            while True:
                menu_emprestimos()

                op3 = int(input("Digite a opção: "))

                if op3 == 1:
                    realizar_emprestimos()
                elif op3 == 2:
                    listar_todos_emprestimos()
                elif op3 == 3:
                    isbn = input("Digite o codigo ISBN: ")
                    buscar_emprestimo_isbn(isbn)
                elif op3 == 0:
                    print("\nRetornando ao menu principal !!!")
                    break
        
        elif op == 0:
            print("\nFinalizando o programa....")
            break






menu()