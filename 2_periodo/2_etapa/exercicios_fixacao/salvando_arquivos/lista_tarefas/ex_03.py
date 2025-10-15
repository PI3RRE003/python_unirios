from model import *
def menu():
    while True:
        print("\n", "="*10," LISTA DE TAREFAS ", "="*10)
        print("1 - Adicionar Tarefas"
              "\n2 - Listar Todas as tarefas"
              "\n3 - Marcar como concluida"
              "\n4 - Listar Tarefas Pendentes"
              "\n5 - Remover Tarefa"
              "\n0 - Sair"
              f"\n{"=" * 40}")

        op = int(input("Digite a opção: "))

        if op == 1:
            adicionar_tarefa()
        elif op == 2:
            listar_todas_tarefas()
        elif op == 3:
            id = input("Digite o ID da tarefa que deseja concluir: ")
            marcar_como_concluida(id)
        elif op == 4:
            listar_pendentes()
        elif op == 5:
            id = input("Digite o ID da tarefa que deseja concluir: ")
            remover_tarefa(id)
        elif op == 0:
            print("Encerrando o programa.....")
            break

menu()