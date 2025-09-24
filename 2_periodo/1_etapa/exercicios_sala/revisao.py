def adicionar_tarefa():
    print("\n============= ADICIONAR TAREFA ============")
    codigo = "00" + str(gerar_codigo())
    descricao = input("Digite a descrição da tarefa: ")
    tarefa = {
        'codigo': codigo,
        'descricao': descricao,
        'status': 'pendente'
    }

    print("\nTAREFA ADICIONADA A LISTA !")
    print(f"\nCodigo:{tarefa['codigo']} - Tarefa: {tarefa['descricao']} ")
    tarefas.append(tarefa)
    print("=============================================")

def gerar_codigo():
    if len(tarefas) == 0:
        cod = 1
    else:
        cod = len(tarefas)+1
    return cod

def marcar_tarefa_como_concluida():
    print("\n======= MARCAR TAREFA COMO CONCLUIDA ======")
    for tarefa in tarefas:
        print(f"Codigo:{tarefa['codigo']} - Tarefa:{tarefa['descricao']} - Status:{tarefa['status']}")

    cod = input("Digite o codigo da tarefa que deseja atualizar: ")
    for tarefa in tarefas:
        if tarefa['codigo'] == cod:
            status = 'concluido'
            tarefa['status'] = status
            print("\nTAREFA MARCADA COMO CONCLUIDA")
            print(f"\nCodigo:{tarefa['codigo']} - Tarefa:{tarefa['descricao']} - Status:{tarefa['status']}")

def listar_tarefas_pendentes():
    pass

tarefas = []
def menu():
    while True:
        print("\n=============== TO DO LIST ===============")
        print("1 - Adicionar tarefa\
            \n2 - Marcar tarefa como concluida\
            \n3 - Listar tarefas pendentes\
            \n4 - Listar todas as tarefas\
            \n0 - Sair")
        print("===========================================")
        
        op = int(input("Digite a opção: "))

        if op == 1:
            adicionar_tarefa()
        elif op == 2:
            marcar_tarefa_como_concluida()
        elif op == 3:
            listar_tarefas_pendentes()
        elif op == 4:
            listar_todas_tarefas()
        elif op == 0:
            print("Encerrando o programa...")
            break

menu()