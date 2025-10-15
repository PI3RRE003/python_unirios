import  json
CONTAS = 'contas.json'
contas = []

def criar_conta(contas):
    print("\n========== CRIANDO CONTA =========")
    nome = input("Digite o nome: ")
    senha = input("Digite a senha: ")
    conta = {
        'nome' : nome,
        'senha' : senha
    }
    contas.append(conta)
    salvar_dados(contas)
    print(f"\nNome:{conta['nome']} - Senha:{conta['senha']}")

def listar_contas():
    try:
        with open(CONTAS, 'r', encoding='utf-8') as arquivo:
            contas_carregadas = json.load(arquivo)
    except FileNotFoundError:
        print(f"O arquivo {CONTAS} não foi encontrado. começando com uma lista vazia")
    except json.JSONDecodeError:
        print(f"O arquivo {CONTAS} esta vazio ou corrompido. começando com uma lista vazia")

    print("========== LISTANDO CONTAS =========")
    for conta in contas_carregadas:
        print(f'Nome:{conta['nome']} - Senha:{conta['senha']}')


def salvar_dados(contas):
    with open(CONTAS, 'w' , encoding='utf-8') as arquivo:
        json.dump(contas, arquivo, indent=4)
    print("Dados salvos com sucesso !!!")

def carregar_dados():
    try:
        with open(CONTAS, 'r', encoding='utf-8') as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return []


def menu():
    print("\n========= CARREGANDO CONTAS =========")
    contas_carregadas = carregar_dados()
    print(f"\nBem vindo ! {len(contas_carregadas)} carregadas do sistema")
    while True:
        print('\n=========== GERENCIAMENTO DE CONTAS ===========')
        print('1 - Criar Conta'
              '\n2 - Listar Contas'
              '\n0 - Sair')
        try:
            op = int(input("Digite a opção: "))
        except ValueError:
            print("Error: Digite um numero valido")
            continue

        if op == 1:
            criar_conta(contas)
        elif op == 2:
            listar_contas()
        elif op == 0:
            print("Finalizando o programa....")
            break

menu()