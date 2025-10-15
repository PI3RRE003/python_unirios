import json

alunos = []
ALUNOS = "alunos.json"

def salvar_dados(alunos):
    with open(ALUNOS, 'w', encoding='utf-8') as arquivo:
        json.dump(alunos, arquivo, indent=4)
    print("Dados salvos com sucesso")

def carregar_dados():
    try:
        with open(ALUNOS, 'r', encoding='utf-8') as arquivo:
            return  json.load(arquivo)
    except FileNotFoundError:
        return []

def cadastrar_aluno():
    print("\n========= CADASTRANDO ALUNO ========")
    id = "00" + str(gerar_codigo())

    nome = input("Digite o nome do aluno: ")
    if valida_nome(nome):
        return

    aluno = {
        'id' : id,
        'nome' : nome,
        'notas' : []
    }
    alunos.append(aluno)
    salvar_dados(alunos)
    print("\nALUNO CADASTRADO COM SUCESSO !!")
    print(f"ID:{aluno['id']} - Nome:{aluno['nome']} - Notas:{aluno['notas']}")

def gerar_codigo():
    if len(alunos) == 0:
        id = 1
    else:
        id = len(alunos)+1
    return id

def valida_nome(nome):
    for numero in nome:
        if numero.isdigit():
            print("Error: nome não pode conter numeros")
            return True

    if not nome:
        print("Error:Campo deve conter nome")
        return True
    return False


def adicionar_nota_aluno(id):
    verificado = verifica_lista_alunos()
    if verificado:
        print("\n========== ADICIONANDO NOTA DO ALUNO ==========")
        for aluno in alunos:
            if aluno['id'] == id:
                nota = float(input("Digite uma nota: "))
                aluno['notas'].append(nota)
                print(f"\nNota:{nota} adicionada com sucesso !!!")
                while True:
                    notas_aluno = aluno['notas']
                    op = input("Deseja adicionar mais uma nota? (S/N): ")
                    if op == 'S'.lower():
                        if verifica_qtd_notas(notas_aluno):
                            return
                        else:
                            nota = float(input("Digite uma nota: "))
                            aluno['notas'].append(nota)
                            print(f"\nNota:{nota} adicionada com sucesso !!!")
                    elif op == 'N'.lower():
                        break
            else:
                print("\nAluno não encontrado, retornando ao menu")
                return
    else:
        print("Error")

def verifica_qtd_notas(notas):
    if len(notas) >= 3:
        print(f"Erro: Aluno ja contem 3 notas: {notas}")
        return True
    return False


def calcular_media_aluno(id):
    verificado = verifica_lista_alunos()
    if verificado:
        print("\n========== CALCULANDO MÉDIA DO ALUNO =========")

        aluno_encontrado = None
        for aluno in alunos:
            if aluno['id'] == id:
                aluno_encontrado = aluno

        if aluno_encontrado:
            notas_aluno = aluno_encontrado['notas']

            if not notas_aluno:
                print(f"O aluno:{aluno_encontrado['nome']} não possui notas")
                return

            media = sum(notas_aluno)/len(notas_aluno)
            print(f"\nA média de:{aluno_encontrado['nome']} é de:{media}")
        else:
            print("Nenhum aluno encontrado")
    else:
        print("Error")

def listar_todos_alunos():
    with open(ALUNOS, 'r', encoding='utf-8') as arquivo:
        alunos_carregados = json.load(arquivo)
    verifica = verifica_lista_alunos()
    if verifica:
        for aluno in alunos_carregados:
            print(f"ID:{aluno['id']} - Nome:{aluno['nome']} - Notas:{aluno['notas']}")
    else:
        print("Error")

def verifica_lista_alunos():
    if not alunos:
        print("Lista de alunos vazia !")
        op = input("Deseja adicionar? (S/N): ")
        if op == 'S'.lower():
            print("\nRedirecionando para o cadastro")
            return cadastrar_aluno()
        elif op == 'N'.lower():
            print("\nRetornando ao menu principal")
            return
    else:
        return True

def menu():
    print("========= CARREGANDO ALUNOS =======")
    alunos = carregar_dados()
    print(f"\nBem vindo ! {len(alunos)} alunos carregados no sistema")
    while True:
        print("\n========= GERENCIADOR DE ALUNOS =========")
        print("1 - Cadastrar Aluno"
              "\n2 - Adicionar Nota a um aluno"
              "\n3 - Calcular média de um aluno"
              "\n4 - Listar todos alunos"
              "\n0 - Sair")
        try:
            op = int(input("Digite a opção: "))
        except ValueError:
            print("Digite uma opção válida 0 a 4")
            continue

        if op == 1:
            cadastrar_aluno()
        elif op == 2:
            id = input("Digite o ID do aluno: ")
            adicionar_nota_aluno(id)
        elif op == 3:
            id = input("Digite o ID do aluno: ")
            calcular_media_aluno(id)
        elif op == 4:
            listar_todos_alunos()
        elif op == 0:
            print("\nFinalizando o programa.......")
            break

menu()
