import os

ALUNOS = 'alunos.txt'

def write_aluno():
    if not os.path.exists(ALUNOS):
        with open(ALUNOS,'w'):
            ...

def append_aluno(nome,matricula,turma):
    with open(ALUNOS,'a') as arquivo:
        linha = f"{nome};{matricula};{turma}\n"
        arquivo.write(linha)

def read_alunos():
    with open(ALUNOS,'r') as arquivo:
        linhas = arquivo.readlines()

        if len(linhas) == 0:
            print("Lista de alunos vazia")
        else:
            for linha in linhas:
                dados = linha.strip().split(";")
                print(f"\nNome:{dados[0]}"
                      f"\nMatricula:{dados[1]}"
                      f"\nTurma:{dados[2]}")



def matricular_aluno():
    print("\n===== MATRICULANDO ALUNO =====")
    nome = input("Digite o nome: ")
    matricula = input("Digite a matricula: ")
    turma = input("Digite a turma/serie: ")

    append_aluno(nome,matricula,turma)
    print(f"\nAluno cadastrando com sucesso !"
          f"\nNome:{nome}"
          f"\nMatricula:{matricula}"
          f"\nTurma:{turma}")

def listar_todos_alunos():
    read_alunos()

def consultar_aluno_pela_matricula(matricula):
    with open(ALUNOS,'r') as arquivo:
        linhas = arquivo.readlines()
        for linha in linhas:
            dados =  linha.strip().split(";")
            if dados[1] == matricula:
                print(f"\nNome:{dados[0]}"
                      f"\nMatricula:{dados[1]}"
                      f"\nTurma:{dados[2]}")
            else:
                print("Aluno não encontrado")


NOTAS = 'notas.txt'

def write_notas():
    if not os.path.exists(NOTAS,'w'):
        ...

def append_notas(aluno, disciplina, nota_1, nota_2, media,status):
    with open(NOTAS, 'a') as arquivo:
        linha = f"{aluno};{disciplina};{nota_1};{nota_2};{media};{status}\n"
        arquivo.write(linha)

def read_notas():
    with open(NOTAS,'r') as arquivo:
        linhas = arquivo.readlines()

        if len(linhas) == 0:
            print("\nLista de notas vazia")
        else:
            for linha in linhas:
                dados = linha.strip().split(";")
                print(f"\nNota 1:{dados[2]}"
                      f"\nNota 2:{dados[3]}"
                      f"\nMédia:{dados[4]}"
                      f"\nStatus:{dados[5]}")




def lançar_notas(matricula):
    print("\n===== LANÇANDO NOTA DO ALUNO =====")
    aluno = consultar_aluno_pela_matricula(matricula)
    disciplina = input("Digite a Disciplina: ")
    nota_1 = float(input("Digite a 1 nota: "))
    nota_2 = float(input("Digite a 2 nota: "))
    media, status = calcula_media(nota_1, nota_2)


    append_notas(aluno,disciplina,nota_1,nota_2, media, status)
    print(f"\nNota do aluno adicionado com sucesso !!!"
          f"\nAluno:{aluno}"
          f"\nDisciplina:{disciplina}"
          f"\nNota 1:{nota_1}"
          f"\nNota 2:{nota_1}"
          f"\nMédia:{media}"
          f"\nStatus:{status}")


def calcula_media(nota_1, nota_2):
    media = (nota_1 + nota_2) / 2

    if media >= 7:
        status = 'Aprovado'
    elif media < 5:
        status = 'Recuperação'
    elif media < 3:
        status = 'Reprovado'
    return media, status

def listar_boletim_geral(matricula):
    print("\n===== LISTANDO BOLETIM GERAL DO ALUNO =====")
    with open(ALUNOS, 'r') as arquivo:
        linhas = arquivo.readlines()
        for linha in linhas:
            dados = linha.strip().split(";")
            if dados[1] == matricula:
                print(f"\nNome:{dados[0]}"
                      f"\nMatricula:{dados[1]}"
                      f"\nTurma:{dados[2]}")
                read_notas()

