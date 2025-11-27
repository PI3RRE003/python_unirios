from model import *

def gerenciar_frota():
    print("\n===== GERENCIANDO FROTAS ====")
    print("1 - Cadastrar Caminhão"
          "\n2 - Listar Frota"
          "\n0 - Sair")

def gerenciar_viagens():
    print("\n==== GERENCIANDO VIAGENS ====")
    print("1 - Registrar Viagem"
          "\n2 - Relatorio Geral"
          "\n3 - Relatorio por Caminhão"
          "\n0 - Sair")

def menu():
    while True:
        print("\n==== DIARIO DE BORDO DA FROTA ====")
        print("1 - Gerenciar Frota"
              "\n2 - Gerenciar Viagens"
              "\n0 - Sair")
        try:
            op = int(input("Digite a opção: "))
            if op == 1:
                while True:
                    gerenciar_frota()

                    op1 = int(input("Digite a opção: "))
                    if op1 == 1:
                        cadastrar_caminhao()
                    elif op1 == 2:
                        listar_frota()
                    elif op1 == 0:
                        print("Retornando ao menu principal....")
                        break
            elif op == 2:
                while True:
                    gerenciar_viagens()

                    op2 = int(input("Digite a opção: "))
                    if op2 == 1:
                        placa = input("Digite a placa da frota: ")
                        registrar_viagem(placa)
                    elif op2 == 2:
                        relatorio_geral()
                    elif op2 == 3:
                        placa = input("Digite a placa da frota: ")
                        relatorio_por_caminhao(placa)
                    elif op2 == 0:
                        print("Retornando ao menu principal...")
                        break
            elif op == 0:
                print("Encerrando o programa...")
                break
        except Exception as e:
            print(f"Error:{e}")

menu()