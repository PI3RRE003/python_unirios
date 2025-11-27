import os

FROTA = 'frota.txt'

def write_frota():
    if not os.path.exists(FROTA):
        with open(FROTA,'w'):
            ...

def append_frota(placa,modelo,capacidade):
    try:
        with open(FROTA,'a') as arquivo:
            linha = f'{placa};{modelo};{capacidade}\n'
            arquivo.write(linha)
    except Exception as e:
        print(f"Error:{e}")

def read_frota():
    try:
        with open(FROTA,'r') as arquivo:
            linhas = arquivo.readlines()

            if len(linhas) == 0:
                print("Lista de frotas vazia")
            else:
                for linha in linhas:
                    dados = linha.strip().split(";")
                    print(f"\nPlaca:{dados[0]}"
                          f"\nModelo:{dados[1]}"
                          f"\nCapacidade:{dados[2]}")
    except Exception as e:
        print(f"Error:{e}")

def cadastrar_caminhao():
    try:
        write_frota()
        print("\n===== CADASTRANDO CAMINHÃO ====")
        placa = input("Digite a placa do caminhão: ")
        modelo = input("Digite o modelo do caminhão: ")
        capacidade = input("Digite a capacidade do caminhão: ")

        append_frota(placa,modelo,capacidade)
        print("Frota cadastrada com sucesso !!!"
              f"\nPlaca:{placa}"
              f"\nModelo:{modelo}"
              f"\nCapacidade:{capacidade}")
    except Exception as e:
        print(f"Error:{e}")

def listar_frota():
    print("\n==== LISTANDO FROTAS ====")
    read_frota()

def buscar_frota_pela_placa(placa):
    print("\n==== BUSCANDO FROTA PELA PLACA ====")
    try:
        with open(FROTA,'r') as arquivo:
            linhas = arquivo.readlines()

            if len(linhas) == 0:
                print("Lista de frotas vazia")
            else:
                for linha in linhas:
                    dados = linha.strip().split(";")
                    if dados[0] == placa:
                        print(f"\nPlaca:{dados[0]}"
                              f"\nModelo:{dados[1]}"
                              f"\nCapacidade:{dados[2]}")
    except Exception as e:
        print(f"Error:{e}")

VIAGENS = 'viagens.txt'

def write_viagens():
    if not os.path.exists(VIAGENS):
        with open(VIAGENS,'w'):
            ...

def append_viagens(placa, destino, quilometros_destino,valor_frete):
    try:
        with open(VIAGENS,'a') as arquivo:
            linha = f'{placa};{destino};{quilometros_destino};{valor_frete}\n'
            arquivo.write(linha)
    except Exception as e:
        print(f"Error:{e}")

def read_viagens():
    try:
        with open(VIAGENS,'r') as arquivo:
            linhas = arquivo.readlines()

            if len(linhas) == 0:
                print("Lista de viagens vazia")
            else:
                for linha in linhas:
                    dados = linha.strip().split(";")
                    print(f"\nPlaca:{dados[0]}"
                          f"\nDestino:{dados[1]}"
                          f"\nQuilometros:{dados[2]}"
                          f"\nValor Frete:{dados[3]}")
    except Exception as e:
        print(f"Error:{e}")

def registrar_viagem(placa):
    print("\n==== REGISTRANDO VIAGEM PELA PLACA ====")
    buscar_frota_pela_placa(placa)

    destino =  input("Digite o destino da frota: ")
    quilometros_destino = input("Digite os KM do destino: ")
    valor_frete = float(input("Digite o valor do frete: "))

    append_viagens(placa,destino,quilometros_destino,valor_frete)
    print("Viagem registrada com sucesso!!"
          f"\nPlaca:{placa}"
          f"\nDestino:{destino}"
          f"\nQuilometros:{quilometros_destino}"
          f"\nValor Frete:{valor_frete}")

def relatorio_geral():
    print("\n==== RELATORIO GERAL DE VIAGENS ====")
    read_viagens()

def relatorio_por_caminhao(placa):
    print("\n==== RELATORIO DE VIAGENS PELA PLACA DA FROTA ====")
    buscar_frota_pela_placa(placa)
    total_frete = 0
    with open(VIAGENS,'r') as arquivo:
        linhas = arquivo.readlines()

        if len(linhas) == 0:
            print("Lista de viagens vazia")
        else:
            for linha in linhas:
                dados = linha.strip().split(";")
                total_frete += float(dados[3])
                if dados[0] == placa:
                    print(f"\nPlaca:{dados[0]}"
                          f"\nDestino:{dados[1]}"
                          f"\nQuilometros:{dados[2]}"
                          f"\nValor Frete:{dados[3]}")
            print(f"\nValor total dos fretes:{total_frete}\n")