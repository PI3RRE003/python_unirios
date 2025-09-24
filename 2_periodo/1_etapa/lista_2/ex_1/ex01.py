from model import *

def registrar_cidade():
    print("\n=========== MENU REGISTRAR CIDADE ==========")
    print("1 - Cadastrar cidade\
          \n2 - Buscar pelo codigo\
          \n3 - Listar todas\
          \n0 - Sair")

def registrar_eleitor():
    print("\n========== MENU REGISTRAR ELEITOR ===========")
    print("1 - Cadastrar eleitor\
          \n2 - Listar todos eleitores\
          \n3 - Buscar Eleitor pelo titulo\
          \n4 - Listar por cidade\
          \n0 - Sair")

def menu():
    while True:
        print("\n=========== MENU ===========")
        print("1 - Registrar Cidade\
              \n2 - Registrar Eleitor\
              \n0 - Sair")
        print("============================")
        
        op = int(input("Digite uma opção: "))

        if op == 1:
            while True:
                
                registrar_cidade()
                
                op1 = int(input("Digite a opção: "))
                
                if op1 == 1:
                    cadastrar_cidade()
                elif op1 == 2:
                    codigo = input("Digite o codigo da cidade: ")
                    buscar_pelo_codigo(codigo)
                elif op1 == 3:
                    listar_todas_cidades()
                elif op1 == 0:
                    print("\nRetornando para o menu principal !!!")
                    break

        elif op == 2:
            while True:
                registrar_eleitor()

                op2 = int(input("Digite a opção: "))
                
                if op2 == 1:
                    cadastrar_eleitor()
                elif op2 == 2:
                    listar_todos_eleitores()
                elif op2 == 3: 
                    titulo = input("Digite o titulo do eleitor: ")
                    buscar_pelo_titulo(titulo)
                elif op2 == 4:
                    cidade = input("Digite a cidade do eleitor: ")
                    listar_por_cidade(cidade)
                elif op2 == 0:
                    print("\nRetornando para o menu principal !!!")
                    break

        elif op == 0:
            print("Finalizando o programa....")
            break

menu()