import os

VEICULOS = "veiculos.txt"

def write_veiciulo():
    try:
        if not os.path.exists(VEICULOS):
            with open(VEICULOS, 'w'):
                ...
    except Exception as e:
        print(f"Error:{e}")

def append_veiculo(modelo,placa,km):
    try:
        with open(VEICULOS, 'a') as arquivos:
            linha = f"{modelo};{placa};{km}\n"
            arquivos.write(linha)
    except Exception as e:
        print("Error:{e} iniciando um arquivo vazio")
        write_veiciulo()

def read_veiculo():
    with open(VEICULOS, 'r') as arquivos:
        linhas = arquivos.readlines()

        if len(linhas) == 0:
            print("Lista de veiculos vazia")
        else:
            for linha in linhas:
                dados = linha.strip().split(";")
                print(f"\nModelo:{dados[0]}"
                      f"\nPlaca:{dados[1]}"
                      f"\nQuilometros:{dados[2]}")
                return dados

"=============================================================================================================="

def cadastrar_veiculo():
    write_veiciulo()

    print("\n===== CADASTRANDO VEICULO =====")

    modelo = input("Digite o modelo do veiculo: ")
    if len(modelo) <= 0:
        print("Campo não pode ser vazio")
        return

    placa = input("Digite o placa do veiculo: ")
    if len(placa) <=0:
        print("Campo não pode ser vazio")
        return


    km = float(input("Digite a quilimetragem do veiculo: "))
    if km < 0:
        print("Quilometros não pode ser negativo")
        return

    append_veiculo(modelo,placa,km)
    print(f"veiculo {modelo} cadastrado com sucesso")



def buscar_pela_placa(placa_veiculo):
    print("\n======= BUSCANDO PELA PLACA =======")
    try:
        with open(VEICULOS, 'r') as arquivos:
            linhas = arquivos.readlines()

            if len(linhas) == 0:
                print("Lista de veiculos vazia")
            else:
                for linha in linhas:
                    dados = linha.strip().split(";")
                    if dados[1] == placa_veiculo:
                        print(f"\nModelo:{dados[0]}"
                              f"\nPlaca:{dados[1]}"
                              f"\nQuilometros:{dados[2]}")
                        return dados
    except Exception as e:
        print(f"Error: {e}")

def listar_todos_veiculos():
    print("===== LISTANDO VEICULOS ======")
    read_veiculo()

"==================================================================================="

SERVICOS = "servicos.txt"

def write_servicos():
    try:
        if not os.path.exists(SERVICOS):
            with open(SERVICOS,'w'):
                ...
    except Exception as e:
        print(f"\nError:{e}")

def append_servicos(codigo_ordem,placa,modelo,tipo_servico):
    try:
        with open(SERVICOS, 'a') as arquivo:
            linha = f"{codigo_ordem};{placa};{modelo};{tipo_servico}\n"
            arquivo.write(linha)
    except Exception as e:
        print(f"\nError:{e}")
        print("Iniciando um arquivo vazio")
        write_servicos()

def read_servicos():
    try:
        with open(SERVICOS, 'r') as arquivo:
            linhas = arquivo.readlines()

            if len(linhas) == 0:
                print("Lista de servicos vazia")
            else:
                for linha in linhas:
                    dados =  linha.strip().split(";")
                    print(f"\nCodigo Ordem:{dados[0]}"
                          f"\nPlaca:{dados[1]}"
                          f"\nModelo:{dados[2]}"
                          f"\nServiço:{dados[3]}")
    except Exception as e:
        print(f"Error:{e}")

def registrar_servico():
    print("===== REGISTRANDO SERVIÇO ======")
    try:
        write_servicos()
        codigo_ordem = gerar_codigo_ordem()

        placa = input("Digite a placa do veiculo: ")

        dado_modelo = buscar_pela_placa(placa)
        modelo = dado_modelo[0]

        tipo_servico = input("Digite o tipo de serviço: ")

        append_servicos(codigo_ordem,placa,modelo,tipo_servico)

        print(f"Servico:{tipo_servico} adicionado com sucesso codigo:{codigo_ordem}")
    except Exception as e:
        print(f"Error: {e}")

def gerar_codigo_ordem():
    with open(SERVICOS, "r") as arquivo:
        linhas = arquivo.readlines()
        codigo_ordem = "S00" + str(len(linhas)+1)
        return  codigo_ordem

def listar_todas_ordens_servico():
    print("===== LISTANDO TODOS SERVIÇOS ======")
    read_servicos()

def buscar_servico_pelo_codigo(cod_servico):
    print("===== BUSCANDO SERVIÇO PELO CODIGO ======")
    try:
        with open(SERVICOS, 'r') as arquivo:
            linhas = arquivo.readlines()

            if linhas == 0:
                print("Nenhum serviço com este codigo, tente novamente")
            else:
                for linha in linhas:
                    dados = linha.strip().split(";")
                    if dados[0] == cod_servico:
                        print(f"\nCodigo Ordem:{dados[0]}"
                              f"\nPlaca:{dados[1]}"
                              f"\nModelo:{dados[2]}"
                              f"\nServiço:{dados[3]}")
    except Exception as e:
        print(f"Error: {e}")

def

