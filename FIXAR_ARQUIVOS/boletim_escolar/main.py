from model import *

def gerenciar_alunos():
    print("\n===== GERENCIANDO ALUNOS =====")
    print("1 - Matricular Aluno"
          "\n2 - Listar todos Alunos"
          "\n3 - Consultar Aluno por Matricula"
          "\n0 - Sair")

def gerenciar_notas():
    print("\n===== GERENCIANDO NOTAS =====")
    print("1 - Lançar Notas "
          "\n2 - Listar Boletim Geral"
          "\n0 - Sair")

def menu():
    while True:
        print("\n===== GERENCIAMENTO DE ALUNOS =====")
        print("1 - Gerenciar Alunos"
              "\n2 - Gerenciar Notas"
              "\n0 - Sair")

        try:
            op = int(input("Digite a opção: "))
            if op == 1:
                while True:
                    gerenciar_alunos()
                    op1 = int(input("Digite a opção: "))
                    if op1 == 1:
                        matricular_aluno()
                    elif op1 == 2:
                        listar_todos_alunos()
                    elif op1 == 3:
                        matricula = input("Digite a matricula do aluno: ")
                        consultar_aluno_pela_matricula(matricula)
                    elif op1 == 0:
                        print("\nRetornando ao menu principal")
                        break
            elif op == 2:
                while True:
                    gerenciar_notas()
                    op2 = int(input("Digite a opção: "))
                    if op2 == 1:
                        matricula = input("Digite a matricula do aluno: ")
                        lançar_notas(matricula)
                    elif op2 == 2:
                        matricula = input("Digite a matricula do aluno: ")
                        listar_boletim_geral(matricula)
                    elif op2 == 0:
                        print("Retornando ao menu principal")
                        break
            elif op == 0:
                print("Encerrando o programa....")
                break
        except Exception as e:
            print(f"{e}")

menu()