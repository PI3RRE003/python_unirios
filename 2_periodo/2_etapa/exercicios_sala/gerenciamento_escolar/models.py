professores = []
def cadastrar_professor():
    print("\n========== CADASTRANDO PROFESSOR ==========")
    try:
        cpf = input("Digite o CPF do professor: ")
        if buscar_professor(cpf):
            print("\nPROFESSOR JA EXISTE")
        else:
            nome = input("Digite o nome do professor: ")
            contato = input("Digite o (email ou telefone): ")

        professor = {
            "NOME" : nome,
            "CPF" : cpf,
            "CONTATO" : contato
        }
        professores.append(professor)
        print(f"\nProfessor:{professor['NOME']}\nCPF:{professor['CPF']}\nTELEFONE:{professor['CONTATO']}\nadicionado com sucesso !")
    except Exception as e:
        print(f"Error:{e}")

def buscar_professor(cpf):
    print("\n=========== BUSCANDO PROFESSOR PELO CPF =============")
    try:
        if len(professores) == 0:
            print("lista de professores vazia")
            return
        else:
            for professor in professores:
                if professor["CPF"] == cpf:
                    print(f"PROFESSOR ENCONTRADO !!!\nProfessor:{professor['NOME']}\nCPF:{professor['CPF']}\nTELEFONE:{professor['CONTATO']}\nadicionado com sucesso !")
                else:
                    print("Professor não encontrado")
    except Exception as e:
        print(f"Error: {e}")

def listar_professores():
    print("\n=========== LISTANDO TODOS OS PROFESSORES ==========")
    try:
        if len(professores) == 0:
            print("lista de professores vazia, retornando ao menu")
            return
        else:
            for professor in professores:
                print(f"\nProfessor:{professor['NOME']}\nCPF:{professor['CPF']}\nTELEFONE:{professor['CONTATO']}\nadicionado com sucesso !")
    except Exception as e:
        print(f"Error: {e}")


alunos = []

def cadastrar_aluno():
    print("\n========== CADASTRANDO ALUNO ==========")
    try:
        cpf = input("Digite o CPF do aluno: ")
        if buscar_aluno(cpf):
            print("\nPROFESSOR JA EXISTE")
        else:
            nome = input("Digite o nome do aluno: ")
            contato = input("Digite o (email ou telefone) do responsavel: ")

        aluno = {
            "NOME" : nome,
            "CPF" : cpf,
            "CONTATO" : contato
        }
        alunos.append(aluno)
        print(f"\nAluno:{aluno['NOME']}\nCPF:{aluno['CPF']}\nTELEFONE:{aluno['CONTATO']}\nadicionado com sucesso !")
    except Exception as e:
        print(f"Error:{e}")

def buscar_aluno(cpf):
    print("\n=========== BUSCANDO ALUNO PELO CPF =============")
    try:
        if len(alunos) == 0:
            print("lista de alunos vazia")
            return
        else:
            for aluno in alunos:
                if aluno["CPF"] == cpf:
                    print(f"ALUNO ENCONTRADO !!!\nAluno:{aluno['NOME']}\nCPF:{aluno['CPF']}\nTELEFONE:{aluno['CONTATO']}")
                else:
                    print("aluno não encontrado")
    except Exception as e:
        print(f"Error: {e}")

def listar_alunos():
    print("\n=========== LISTANDO TODOS OS ALUNOS ==========")
    try:
        if len(alunos) == 0:
            print("lista de alunos vazia, retornando ao menu")
            return
        else:
            for aluno in alunos:
                print(f"\nAluno:{aluno['NOME']}\nCPF:{aluno['CPF']}\nTELEFONE:{aluno['CONTATO']}")
    except Exception as e:
        print(f"Error: {e}")


disciplinas = []

def cadastrar_disciplina():
    try:
        cod = "D0" + str(len(disciplinas)+1)
        nome = input("Digite o nome da disciplina: ")
        cpf = input("Digite o CPF do professor:")
        if buscar_professor(cpf):
            for professor in professores:
                disciplina = {
                    "COD" : cod,
                    "NOME" : nome,
                    "PROF" : professor['NOME']
                }
                disciplinas.append(disciplina)
        else:
            print("Prodessor não encontrado")
    except Exception as e:
        print(f"Error:{e}")


def listar_disciplinas():
    if len(disciplinas) == 0:
        print("Error: lista de disciplinas vazias")
    else:
        for disciplina in disciplinas:
            print(f"DISCIPLINA"
                  f"\nCOD:{disciplina['COD']}"
                  f"\nProfessor: CPF:{disciplina['CPF']} Nome:{disciplina['NOME']}")


def buscar_disciplina(cod):
    if len(disciplinas) == 0:
        print("Error: lista de disciplinas vazias")
    else:
        for disciplina in disciplinas:
            if disciplina['COD'] == cod:
                print(f"DISCIPLINA"
                      f"\nCOD:{disciplina['COD']}"
                      f"\nProfessor: CPF:{disciplina['CPF']} Nome:{disciplina['NOME']}")
            else:
                print("Professor não encontrado")