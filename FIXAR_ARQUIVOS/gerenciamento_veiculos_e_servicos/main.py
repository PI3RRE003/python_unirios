from models import *
def gerenciar_veiculos():
    print("\n====== GERENCIAR VEICULOS =====")
    print("1 - Cadastrar veiculo"
          "\n2 - Buscar veiculo pela placa "
          "\n3 - Listar todos veiculos"
          "\n0 - Sair")

def gerenciar_ordens():
    print("\n===== GERENCIAR ORDENS =====")
    print("1 -  Registrar ordem de serviço"
          "\n2 -  Listar todas ordens de serviço"
          "\n3 -  Buscar pelo codigo da ordem de serviço"
          "\n0 - Sair")


def menu():
    while True:
        print("\n===== MENU =====")
        print("1 - Gerenciar Veiculos"
              "\n2 - Gerenciar Ordens"
              "\n0 - Sair")
        try:
            op = int(input("Digite a opção: "))

            if op == 1:
                while True:
                    gerenciar_veiculos()

                    op1 = int(input("Digite a opção: "))

                    if op1 == 1:
                        cadastrar_veiculo()
                    elif op1 == 2:
                        placa = input("Digite a placa do veiculo que deseja buscar: ")
                        buscar_pela_placa(placa)
                    elif op1 == 3:
                        listar_todos_veiculos()
                    elif op1 == 0:
                        print("Retornando ao menu principal...")
                        break
                    else:
                        print("Digite apenas de 0 a 3")
            elif op == 2:
                while True:
                    gerenciar_ordens()

                    op2 = int(input("Digite a opção: "))

                    if op2 == 1:
                        registrar_servico()
                    elif op2 == 2:
                        listar_todas_ordens_servico()
                    elif op2 == 3:
                        cod_servico = input("Digite o codigo de servico: ")
                        buscar_servico_pelo_codigo(cod_servico)
                    elif op2 == 0:
                        print("Retornado ao menu principal...")
                        break
                    else:
                        print("Digite apenas de 0 a 3")
            elif op == 0:
                print("\nEncerrando o programa")
                break
        except Exception as e:
            print(f"Error: {e}")
        except ValueError:
            print("Digite apenas numeros")

menu()