def menu():
    print("\n===== GERENCIAMENTO ESCOLAR =====")
    print("1 - Professor"
          "\n2 - Aluno"
          "\n3 - Disciplina"
          "\n0 - Sair")

def menu_professor():
    print("\n====== MENU PROFESSOR =====")
    print("1 - Cadastrar Professor"
          "\n2 - Buscar Professor"
          "\n3 - Listar Professores"
          "\n0 - Sair")


def main():
    while True:
        menu()

        try:
            op = int(input("Digite uma opção: "))

            if op == 1:
                while True:
                    menu_professor()

                    op1 = int(input("Digite a opção: "))

                    if op1 == 1:
                        cadastrar_professor()
                    elif op1 == 2:
                        buscar_professor()
                    elif op1 == 3:
                        listar_professores()
                        
            elif op == 2:
                ...
            elif op == 3:
                ...
            elif op == 0:
                print("Encerrando o programa....")
                break
            else:
                print("Opção Invalida !")
        except ValueError:
            print("Error: Digite apenas numeros")
        except Exception as e:
            print(f"Error:{e}")