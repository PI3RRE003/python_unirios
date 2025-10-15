from model import *
def menu():
    while True:
        print("\n========== CONTROLE DE FREQUENCIA ========")
        print("1 - Cadastrar Aluno"
              "\n2 - Lançar Falta"
              "\n3 - Listar Alunos"
              "\n4 - Buscar Aluno"
              "\n5 - Alterar Nome"
              "\n0 - Sair")

        op = int(input("Digite a opção: "))

        if op == 1:
            cadastrar_aluno()
        elif op == 2:
            matricula = input("Digite a matricula do aluno: ")
            lancar_falta(matricula)
        elif op == 3:
            listar_aluno()
        elif op == 4:
            matricula = input("Digite a matricula do aluno: ")
            buscar_aluno(matricula)
        elif op == 5:
            matricula = input("Digite a matricula do aluno: ")
            alterar_nome(matricula)
        elif op == 0:
            print("Encerrando o programa....")
            break


menu()