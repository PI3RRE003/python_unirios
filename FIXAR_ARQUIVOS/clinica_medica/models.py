#ARQUIVOS - WAR - IMPORT OS
#VALIDACOES
import os

PACIENTES = 'pacientes.txt'

def write_pacientes():
    try:
        if not os.path.exists(PACIENTES):
            with open(PACIENTES,'w'):
                print("\nCriando arquivo de pacientes\n")
    except Exception as e:
        print(f"Error:{e}")

def append_pacientes(codigo_paciente,nome,idade,telefone):
    with open(PACIENTES,'a') as arquivo:
        linha = f"{codigo_paciente};{nome};{idade};{telefone}\n"
        arquivo.write(linha)

def read_pacientes():
    with open(PACIENTES,'r') as arquivo:
        linhas = arquivo.readlines()

        if len(linhas) == 0:
            print("Lista de pacientes vazia")
        else:
            for linha in linhas:
                dados = linha.strip().split(";")
                print(f"\nCodigo do Paciente:{dados[0]}"
                      f"\nNome do Paciente:{dados[1]}"
                      f"\nIdade do Paciente:{dados[2]}"
                      f"\nTelefone do Paciente:{dados[3]}")
                return dados

def cadastrar_paciente():
    write_pacientes()
    print("\n===== CADASTRANDO PACIENTE =====")
    try:
        codigo_paciente = gerar_codigo_paciente()

        nome = input("Digite o nome do paciente: ")
        if len(nome) == 0:
            print("Campo não pode ser vazio")
            return

        idade = int(input("Digite a idade: "))

        telefone =  input("Digite o telefone do paciente: ")
        if len(telefone) == 0:
            print("Campo não pode ser vazio")
            return

        append_pacientes(codigo_paciente,nome,idade,telefone)
        print(f"\nPaciente {nome} adicionado com sucesso!!!")
    except Exception as e:
        print(f"Error:{e}")

def gerar_codigo_paciente():
    try:
        with open(PACIENTES,'r') as arquivo:
            linha = arquivo.readlines()
            codigo_paciente =  "P00" + str(len(linha)+1)
            return  codigo_paciente
    except Exception as e:
        print(f"Error:{e}")

def listar_pacientes():
    read_pacientes()

def buscar_paciente_pelo_codigo(codigo_paciente):
    dado = read_pacientes()
    if dado[0] == codigo_paciente:
        return dado
    else:
        print("Paciente não encontrado")

CONSULTAS = 'consultas.txt'

def write_consultas():
    try:
        if not os.path.exists(CONSULTAS):
            with open(CONSULTAS,'w'):
                print("\nCriando arquivo de consultas\n")
    except Exception as e:
        print(f"Error:{e}")

def append_consultas(paciente,tipo_consulta):
    with open(CONSULTAS,'a') as arquivo:
        linha = f"{paciente};{tipo_consulta}\n"
        arquivo.write(linha)

def read_consultas():
    with open(CONSULTAS,'r') as arquivo:
        linhas = arquivo.readlines()

        if len(linhas) == 0:
            print("Lista de consultas vazia")
        else:
            for linha in linhas:
                dados = linha.strip().split(";")
                print(f"\nCodigo do Paciente:{dados[0]}"
                      f"\nNome do Paciente:{dados[1]}"
                      f"\nIdade do Paciente:{dados[2]}"
                      f"\nTelefone do Paciente:{dados[3]}")
                return dados

def agendar_consulta():
    codigo_paciente = input("Digite o codigo do paciente: ")
    if len(codigo_paciente) == 0:
        print("Campo não pode ser vazio")
    paciente = buscar_paciente_pelo_codigo(codigo_paciente)

    tipo_consulta = input("Digite o tipo de consulta: ")
    if len(tipo_consulta) == 0:
        print("Campo não pode ser vazio")

    append_consultas(paciente,tipo_consulta)
    print(f"Consulta {tipo_consulta} realizada para {paciente}")

def listar_consulta():
    read_consultas()

def cancelar_consulta():
    ...

def buscar_consulta_pelo_codigo(codigo_consulta):
    dado = read_consultas()
    if dado[0] == codigo_consulta:
        return dado
    else:
        print("Nenhuma consulta encontrada")