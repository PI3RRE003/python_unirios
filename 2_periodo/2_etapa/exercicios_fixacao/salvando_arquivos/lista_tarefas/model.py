import csv

TAREFAS = 'tarefas.csv'

def salvar_dados(tarefas):
    with open(TAREFAS, 'w', newline='', encoding='utf-8')as arquivo:
        cabecalho = ['id', 'descricao', 'status', 'prioridade']
        escritor_csv = csv.DictWriter(arquivo, fieldnames=cabecalho)
        escritor_csv.writeheader()
        escritor_csv.writerows(tarefas)

def carregar_dados():
    tarefas = []
    try:
        with open(TAREFAS, 'r', newline='', encoding='utf-8') as arquivo:
            tarefas_csv = csv.DictReader(arquivo)
            for linha in tarefas_csv:
                tarefas.append(linha)
    except FileNotFoundError:
        ...
    return tarefas

def adicionar_tarefa():
    print(f"\n{"=" * 10} ADICIONANDO TAREFA {"=" * 10}")

    id = "00" + str(gerar_id())
    descricao = input("Digite a descrição da tarefa: ")
    status = 'pendente'
    prioridade = int(input("Digite a prioridade: 1-baixa 2-média 3-alta: "))

    tarefa = {
        'id' : id,
        'descricao' : descricao,
        'status' : status,
        'prioridade' : definir_prioridade(prioridade)
    }
    tarefas = carregar_dados()
    tarefas.append(tarefa)
    salvar_dados(tarefas)
    print("\nTAREFA ADICIONADA COM SUCESSO !")
    print(f"ID:{tarefa['id']} - Descrição:{tarefa['descricao']} - Status:{tarefa['status']} - Prioridade:{tarefa['prioridade']}")

def gerar_id():
    tarefas = carregar_dados()
    if not tarefas:
        id = 1
    else:
        id = len(tarefas)+1
    return id

def definir_prioridade(prioridade):
    if prioridade == 1:
        prioridade = 'Baixa'
    elif prioridade == 2:
        prioridade = 'Média'
    elif prioridade == 3:
        prioridade = 'Alta'
    return prioridade

def listar_todas_tarefas():
    print(f"\n{"=" * 10} LISTANDO TAREFAS {"=" * 10}")
    nao_existe = verificar_existencia_de_tarefa()
    if nao_existe:
        return

    tarefas = carregar_dados()
    for tarefa in tarefas:
        print(f"ID:{tarefa['id']} - Descrição:{tarefa['descricao']} - Status:{tarefa['status']} - Prioridade:{tarefa['prioridade']}")

def marcar_como_concluida(id):
    tarefas = carregar_dados()
    print(f"\n{"=" * 10} CONCLUINDO TAREFA {"=" * 10}")
    nao_existe = verificar_existencia_de_tarefa()
    if nao_existe:
        return
    else:
        for tarefa in tarefas:
            if tarefa['id'] == id:
                tarefa['status'] = 'Concluida'
                print(f"ID:{tarefa['id']} - Descrição:{tarefa['descricao']} - Status:{tarefa['status']} - Prioridade:{tarefa['prioridade']}")
                salvar_dados(tarefas)

def listar_pendentes():
    tarefas = carregar_dados()
    print(f"\n{"=" * 10} LISTANDO TAREFAS PENDENTES{"=" * 10}")
    nao_existe = verificar_existencia_de_tarefa()
    if nao_existe:
        return
    else:
        for tarefa in tarefas:
            if tarefa['status'] == 'pendente'.lower():
                print(f"ID:{tarefa['id']} - Descrição:{tarefa['descricao']} - Status:{tarefa['status']} - Prioridade:{tarefa['prioridade']}")


def remover_tarefa(id):
    tarefas = carregar_dados()
    print(f"\n{"=" * 10} REMOVENDO TAREFA {"=" * 10}")
    nao_existe = verificar_existencia_de_tarefa()
    if nao_existe:
        return
    else:
        for tarefa in tarefas:
            if tarefa['id'] == id:
                tarefas.remove(tarefa)
                print(f"Tarefa removida: {tarefa['descricao']}")
                salvar_dados(tarefas)

def verificar_existencia_de_tarefa():
    tarefas = carregar_dados()
    if not tarefas:
        print("\nLista de tarefas vazia !!")
        op = input("Deseja adicionar? (S/N): ")

        if op == 'S'.lower():
            return adicionar_tarefa()
        elif op == 'N'.lower():
            print("\nRetornando ao menu..")
            return


