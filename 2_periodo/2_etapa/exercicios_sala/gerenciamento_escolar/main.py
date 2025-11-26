from models import *

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

def menu_aluno():
    print("\n========== MENU ALUNO ==========")
    print("1 - Cadastrar Listar"
          "\n2 - Buscar Aluno"
          "\n3 - Listar Alunos"
          "\n0 - Sair")

def menu_disciplina():
    print("\n========== MENU DISCIPLINA ===========")
    print("1 - Cadastrar disciplina"
          "\n2 - Listar disciplinas"
          "\n3 - Buscar disciplina"
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
                        cpf = input("Digite o CPF do professor que deseja buscar: ")
                        buscar_professor(cpf)
                    elif op1 == 3:
                        listar_professores()

            elif op == 2:
                while True:
                    menu_aluno()

                    try:
                        op2 = int(input("Digite a opção: "))

                        if op2 == 1:
                            cadastrar_aluno()
                        elif op2 == 2:
                            cpf = input("Digite o cpf do aluno")
                            buscar_aluno(cpf)
                        elif op2 == 3:
                            listar_alunos()
                        elif op2 == 0:
                            print("\nRetornando ao menu principal...")
                            return
                    except ValueError:
                        print("Digite apenas numeros")
                    except Exception as e:
                        print(f"Error: {e}")
            elif op == 3:
                while True:
                    menu_disciplina()

                    try:
                        op3 = int(input("Digite a opção: "))

                        if op3 == 1:
                            cadastrar_disciplina()
                        elif op3 == 2:
                            listar_disciplinas()
                        elif op3 == 3:
                            cod = input("Digite o codigo da disciplina: ")
                            buscar_disciplina(cod)
                        elif op3 == 0:
                            print("Retornando ao menu principal...")
                            break
                    except ValueError:
                        print("Error: digite apenas numeros")
                    except Exception as e:
                        print(f"Error: {e}")
            elif op == 0:
                print("Encerrando o programa....")
                break
            else:
                print("Opção Invalida !")
        except ValueError:
            print("Error: Digite apenas numeros")
        except Exception as e:
            print(f"Error:{e}")

main()