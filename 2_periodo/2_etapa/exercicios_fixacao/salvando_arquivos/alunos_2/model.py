import csv

ALUNOS = 'alunos.csv'

def carregar_dados():
    alunos = []
    try:
        with open(ALUNOS, 'r', newline='', encoding='utf-8') as arquivo:
            alunos_csv = csv.DictReader(arquivo)
            for linha in alunos_csv:
                alunos.append(linha)
    except FileNotFoundError:
        ...
    return alunos

def salvar_dados(alunos):
    with open(ALUNOS, 'w', newline='', encoding='utf-8') as arquivo:
        cabecalho = ['matricula', 'nome', 'faltas']
        escritor_csv = csv.DictWriter(arquivo, fieldnames=cabecalho)

        escritor_csv.writeheader()

        escritor_csv.writerows(alunos)


def cadastrar_aluno():
    print("\n========= CADASTRANDO ALUNO =========")
    matricula = "00" + str(gerar_matricula())
    nome = input("Digite o nome do aluno: ")
    total_faltas = 0

    aluno = {
        'matricula' : matricula,
        'nome' : nome,
        'faltas' : total_faltas
    }

    alunos = carregar_dados()
    alunos.append(aluno)
    salvar_dados(alunos)
    print("\nALUNO CADASTRADO COM SUCESSO !")
    print(f"Matricula:{aluno['matricula']} - Nome:{aluno['nome']} - Faltas:{aluno['faltas']}")

def gerar_matricula():
    alunos = carregar_dados()

    if not alunos:
        matricula = 1
    else:
        matricula = len(alunos)+1
    return matricula

def lancar_falta(matricula):
    print("\n======== LANÇANDO FALTA ========")
    alunos = carregar_dados()
    encontrado = False
    for aluno in alunos:
        if aluno['matricula'] == matricula:
            print(f"\nALUNO ENCONTRADO !\nMatricula:{aluno['matricula']} - Nome:{aluno['nome']} - Faltas:{aluno['faltas']}")
            try:
                falta_atual = int(aluno['faltas'])

                falta_adicionar = int(input(f"\nDigite a quantidade de faltas de {aluno['nome']} : "))

                aluno['faltas'] = falta_atual + falta_adicionar

                salvar_dados(alunos)

                print(f"\nFalta atualizada de:{aluno['nome']} adicionado {aluno['faltas']} faltas")
                encontrado = True
                break
            except ValueError:
                print("\nError: Digite um numero valido de faltas")
        if not encontrado:
            print("\nAluno não encontrado")

def listar_aluno():
    print("\n======== LISTANDO ALUNOS ========")
    alunos = carregar_dados()
    if not alunos:
        print("\nnenhum aluno encontrado")
        return
    else:
        for aluno in alunos:
            print(f"\nMatricula:{aluno['matricula']} - Nome:{aluno['nome']} - Faltas:{aluno['faltas']}")

def buscar_aluno(matricula):
    print("\n========= BUSCANDO ALUNO =========")
    alunos = carregar_dados()
    encontrado = False
    if not alunos:
        print("\nnenhum aluno encontrado")
        return
    else:
        for aluno in alunos:
            if aluno['matricula'] == matricula:
                print(f"\nALUNO ENCONTRADO !\nMatricula:{aluno['matricula']} - Nome:{aluno['nome']} - Faltas:{aluno['faltas']}")
                encontrado = True
                break

        if not encontrado:
            print("\nAluno não encontrado")

def alterar_nome(matricula):
    print("\n========== ALTERANDO NOME DO ALUNO =========")
    alunos = carregar_dados()
    encontrado = False

    for aluno in alunos:
        if aluno['matricula'] == matricula:
            print(f"\nALUNO ENCONTRADO !\nMatricula:{aluno['matricula']} - Nome:{aluno['nome']} - Faltas:{aluno['faltas']}")

            nome = input(f"Digite o nome atualizado de {aluno['nome']}: ")
            aluno['nome'] = nome
            salvar_dados(alunos)
            print(f"\nNome alterado: {aluno['nome']}")
            encontrado = True
            break

    if not encontrado:
        print("\nAluno não encontrado")

