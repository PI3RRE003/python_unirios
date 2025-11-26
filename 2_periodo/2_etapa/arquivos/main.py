import os

ARQUIVO = "pessoas.txt"

def criar_arquivo():
    if not os.path.exists(ARQUIVO):
        with open(ARQUIVO, 'w'):
            pass

def salvar_arquivo(nome, cpf):
    with open(ARQUIVO, 'a') as arquivo:
        linha = f"{nome};{cpf}\n"
        arquivo.write(linha)

def carregar_arquivo():
    with open(ARQUIVO, 'r') as arquivo:
        linhas = arquivo.readlines()

        if len(linhas) == 0:
            print("Nenhuma pessoa cadastrada !")
        else:
            for linha in linhas:
                dados = linha.strip().split(";")
                print(f"Nome: {dados[0]} - CPF: {dados[1]}")


def cadastrar_pessoa():
    criar_arquivo()
    nome = input("Digite o nome:")
    cpf = input("Digite o CPF:")
    salvar_arquivo(nome, cpf)
    print("Pessoa cadastrada com sucesso !!!")

def listar_pessoas():
    carregar_arquivo()


def buscar_pessoa_pelo_cpf(cpf):
    dados = carregar_arquivo()
    for dado in dados:
        if dado[1] == cpf:
            print(f"Nome: {dados[0]} - CPF: {dados[1]}")


def menu():
    while True:
        print("\n===== MENU =====")
        print("1 - Cadastrar Pessoa"
              "\n2 - Listar Pessoas"
              "\n3 - Buscar Pessoas"
              "\n0 - Sair")
        try:
            op = int(input("Digite uma opção: "))

            if op == 1:
                cadastrar_pessoa()
            elif op == 2:
                listar_pessoas()
            elif op == 3:
                cpf = input("Digite o CPF: ")
                buscar_pessoa_pelo_cpf(cpf)
            elif op == 0:
                print("Encerrando o programa...")
                break
            else:
                print("Digite uma opção de 0 a 3")
        except Exception as e:
            print(f"Error:{e}")
        except ValueError:
            print("Error: Digite apenas numeros")

menu()