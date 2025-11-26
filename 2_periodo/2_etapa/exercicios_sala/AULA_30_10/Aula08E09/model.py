#Professor --------------------------
import os
professores = [] #[{}, {}, {}...]
def cadastrar_professor():
    print("--- CADASTRO DE PROFESSORES ---")
    try:
        cpf = input("Informe o CPF: ")
        if buscar_professor(cpf):
            print("ERRO! CPF já existe.")
        else:
            nome = input("Informe o nome do professor: ")
            contato = input("Informe o contato (e-mail ou telefone): ")
            professor = {"NOME": nome, "CPF": cpf, "CONTATO": contato}
            professores.append(professor)
    except Exception as erro:
        print(f"ERRO: {erro}")

def listar_professores():
    print("--- LISTAGEM DE PROFESSORES ---")
    if len(professores) == 0:
        print("Nenhum professor foi cadastrado.")
    else:
        for p in professores:
            print("PROFESSOR:")
            print(f"Nome: {p['NOME']} - CPF: {p['CPF']} - Contato: {p['CONTATO']}")

def buscar_professor(cpf):
    print("--- BUSCAR PROFESSOR ---")
    for p in professores:
        if cpf == p['CPF']:
            print("PROFESSOR encontrado:")
            print(f"Nome: {p['NOME']} - CPF: {p['CPF']} - Contato: {p['CONTATO']}")
            return True

    print("Professor não encontrado!")
    return False


# Aluno-----------------------------------------------------------------------------
alunos = []

def cadastrar_aluno():
    print("--- CADASTRO DE ALUNO ---")
    cpf = input("Informe o CPF: ")
    if buscar_aluno(cpf):
        print("Não é possível cadastrar, pois esse CPF já existe!")
    else:
        nome = input("Informe o nome: ")
        telefone = int(input("Informe o telefone: "))
        aluno = {"NOME": nome, "CPF": cpf, "FONE": telefone}
        alunos.append(aluno)
        print(f"Aluno {nome} cadastrado com sucesso!")

def listar_aluno():
    print("--- LISTAGEM DE ALUNOS ---")
    if len(alunos) == 0:
        print("Nenhum aluno foi cadastrado.")
    else:
        for a in alunos:
            print(f"\nNome: {a['NOME']}\n CPF: {a['CPF']}\n Telefone: {a['FONE']}")

def buscar_aluno(cpf):
    print("--- BUSCAR ALUNO ---")
    for a in alunos:
        if a["CPF"] == cpf:
            print(f"\nNome: {a['NOME']}\n CPF: {a['CPF']}\n Telefone: {a['FONE']}")
            return True
    print("Aluno não cadastrado!")
    return False


#Disciplina---------------------------------------------
disciplinas = []

def cadastrar_disciplina():
    print("--- CADASTRO DE DISCIPLINA ---")
    cod = "D0"+str(len(disciplinas)+1)
    nome = input("Informe o nome do disciplina: ")

    cpf = input("Informe o CPF do professor: ")
    if buscar_professor(cpf):
        for p in professores:
            if cpf == p['CPF']:
                disciplina = {"COD": cod, "NOME": nome, "CPF": cpf, "PROF": p["NOME"]}
                disciplinas.append(disciplina)
    else:
        print("ERRO! Por favor tente novamente.")

def listar_disciplinas():
    print("--- LISTAGEM DE DISCIPLINAS ---")
    if len(disciplinas) == 0:
        print("Nenhum disciplina foi cadastrada.")
    else:
        for d in disciplinas:
            print(f"DISCIPLINA {d['COD']}:")
            print(f"Nome: {d['NOME']} - Professor: {d['PROF']} (CPF: {d['CPF']})")

def buscar_disciplina(cod):
    print("--- BUSCAR DISCIPLINA ---")
    for d in disciplinas:
        if d["COD"] == cod:
            print(f"DISCIPLINA {d['COD']}:")
            print(f"Nome: {d['NOME']} -  Professor: {d['PROF']} (CPF: {d['CPF']})")
            return True

    print("Código não encontrado!")
    return False

def listar_disciplinas_por_professor(cpf):
    print("--- LISTAGEM POR PROFESSOR ---")
    if buscar_professor(cpf):
        encontrado = False
        for d in disciplinas:
            if cpf == d["CPF"]:
                print(f"DISCIPLINA {d['COD']}:")
                print(f"Nome: {d['NOME']} -  Professor: {d['PROF']} (CPF: {d['CPF']})")
                encontrado = True

        if encontrado == False:
            print("Não há disciplinas vinculadas a esse professor!")
    else:
        print("Erro! CPF não cadastrado!")

#Matriculas ----------------------------------------------------------------------

MATRICULAS = "matriculas.txt"

def gerar_arquivo_matricula():
    if not os.path.exists(MATRICULAS):
        with open(MATRICULAS, 'w') as arquivo:
            pass

def carregar_arquivo_matricula():
    with open(MATRICULAS, 'r') as arquivos:
        linhas = arquivos.readlines()

        if len(linhas) == 0:
            print("Nenhuma matricula")
        else:
            for linha in linhas:
                dados = linha.strip().split(";")
                print(f"Matricula:{dados[0]}"
                      f"\nDisciplina:{dados[1]}"
                      f"\nCodigo disciplina:{dados[2]}"
                      f"\nAluno:{dados[3]}"
                      f"\nCPF:{dados[4]}\n")

def gerar_codigo_matricula():
    with open(MATRICULAS, "r") as arquivo:
        linha = arquivo.readlines()
        codigo = "M0" + str(len(linha)+1)
        return codigo

def gerar_matricula(cod_matr, nome_disci, cod_disci, nome_aluno,cpf):
    with open(MATRICULAS, 'a') as arquivo:
        linha = f"{cod_matr};{nome_disci};{cod_disci};{nome_aluno};{cpf}"
        arquivo.write(linha)
        print("Matricula realizada com sucesso")

def realizar_matricula():
    gerar_arquivo_matricula()
    print("--- REALIZANDO MATRICULA ---")
    cpf = input("Informe o CPF do aluno: ")

    if not buscar_aluno(cpf):
        print("Error")
        return

    for aluno in alunos:
        if aluno['CPF'] == cpf:
            nome_aluno = aluno["NOME"]

    cod_disciplina = input("Informe o codigo da disciplina: ")
    if not buscar_disciplina(cod_disciplina):
        print("Error")
        return

    for disciplina in disciplinas:
        nome_disciplina = disciplina["NOME"]

    codigo = gerar_codigo_matricula()

    gerar_matricula(codigo,nome_disciplina,cod_disciplina,nome_aluno,cpf)

def buscar_matricula(cod):
    print("--- BUSCAR MATRICULA ---")


def listar_matriculas():
    print("--- LISTAGEM DE MATRICULAS ---")
    carregar_arquivo_matricula()


def listar_matriculas_aluno(cpf):
    print("--- LISTAGEM DE MATRICULAS ALUNOS ---")
    if buscar_aluno(cpf):
        encontrado = False
        for m in matriculas:
            if cpf == m["CPF"]:
                print(f"\nMATRICULA {m['COD']}:")
                print(f"Aluno: {m['ALUNO']} - Disciplina: {m['DISCIPLINA']}")
                encontrado = True

        if encontrado == False:
            print("Não há matriculas vinculadas a esse aluno!.")
    else:
        print("ERRO! CPF não encontrado!.")

def listar_matriculas_disciplina(cod):
    print("--- LISTAGEM DE MATRICULAS POR DISCIPLINA ---")
    if buscar_disciplina(cod):
        encontrado = False

        for m in matriculas:
            if cod == m["COD_DISCIPLINA"]:
                print(f"\nMATRICULA {m['COD']}:")
                print(f"Aluno: {m['ALUNO']} - Disciplina: {m['DISCIPLINA']}")
                encontrado = True

        if encontrado == False:
            print("Não há matriculas para essa disciplina!")
    else:
        print("ERRO!")