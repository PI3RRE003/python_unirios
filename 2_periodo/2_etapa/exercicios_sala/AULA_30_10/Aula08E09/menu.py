from model import *
def menu():
    print("=======MENU========")
    print("1. Professor")
    print("2. Aluno")
    print("3. Disciplina")
    print("4. Matricula")
    print("0. Sair")

def menu_professor():
    print("=======MENU PROFESSOR========")
    print("1. Cadastrar Professor")
    print("2. Buscar Professor")
    print("3. Listar Professores")
    print("0. Sair")

def menu_aluno():
    print("=======MENU ALUNO========")
    print("1. Cadastrar Aluno")
    print("2. Buscar Aluno")
    print("3. Listar Alunos")
    print("0. Sair")

def menu_disciplina():
    print("=======MENU DISCIPLINA========")
    print("1. Cadastrar Disciplina")
    print("2. Buscar Disciplina")
    print("3. Listar Disciplinas")
    print("4. Listar Disciplinas por Professor")
    print("0. Sair")

def menu_matriculas():
    print("=======MENU MATRICULAS========")
    print("1. Realizar Matricula")
    print("2. Listar Todas Matriculas")
    print("3. Buscar Matricula pelo Código")
    print("4. Listar Matriculas por Aluno")
    print("5. Listar Matriculas por Disciplina")
    print("0. Sair")

def main():
    while True:
        menu()
        try:
            op = int(input(">>> "))
            if op == 1:
                while True:
                    menu_professor()
                    op2 = int(input(">>> "))
                    if op2 == 1:
                        cadastrar_professor()
                    elif op2 == 2:
                        cpf = input("Informe o CPF: ")
                        buscar_professor(cpf)
                    elif op2 == 3:
                        listar_professores()
                    elif op2 == 0:
                        print("Saindo do menu de professor...")
                        break
                    else:
                        print("Opção Inválida!")
            elif op == 2:
                while True:
                    menu_aluno()
                    op2 = int(input(">>> "))
                    if op2 == 1:
                        cadastrar_aluno()
                    elif op2 == 2:
                        cpf = input("Informe o CPF: ")
                        buscar_aluno(cpf)
                    elif op2 == 3:
                        listar_aluno()
                    elif op2 == 0:
                        print("Saindo do menu de professor...")
                        break
                    else:
                        print("Opção Inválida!")
            elif op == 3:
                while True:
                    menu_disciplina()
                    op3 = int(input(">>> "))

                    if op3 == 1:
                        cadastrar_disciplina()
                    elif op3 == 2:
                        cod = input("Informe o Código: ")
                        buscar_disciplina(cod)
                    elif op3 == 3:
                        listar_disciplinas()
                    elif op3 == 0:
                        print("Saindo do menu de disciplina...")
                        break
                    elif op3 == 4:
                        cpf = input("Informe o CPF: ")
                        listar_disciplinas_por_professor(cpf)
                    else:
                        print("Opção inválida!")

            elif op == 4:
                while True:
                    menu_matriculas()
                    op4 = int(input(">>> "))
                    if op4 == 1:
                        realizar_matricula()
                    elif op4 == 2:
                        listar_matriculas()
                    elif op4 == 3:
                        cod = input("Informe o código da matrícula: ")
                        buscar_matricula(cod)
                    elif op4 == 4:
                        cpf = input("Informe o CPF do aluno: ")
                        listar_matriculas_aluno(cpf)
                    elif op4 == 5:
                        cod = input("Informe o código da discipina: ")
                        listar_matriculas_disciplina(cod)
                    elif op4 == 0:
                        print("Saindo do menu de matriculas...")
                        break
                    else:
                        print("Opção inválida!")
            elif op == 0:
                print("Encerrando porgrama...")
                break
            else:
                print("Opção Inválida!")

        except ValueError:
            print("ERRO de valor!")
        except Exception as e:
            print(f"ERRO Genérico: {e}")

main()