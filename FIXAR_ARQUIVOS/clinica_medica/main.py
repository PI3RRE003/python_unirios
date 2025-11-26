#MENU E IMPORT MODELS
from models import  *

def menu_paciente():
    print("\n===== MENU PACIENTES =====")
    print("1 - Cadastrar Paciente"
          "\n2 - Listar Pacientes"
          "\n3 - Buscar Paciente pelo Codigo"
          "\n0 - Retornar ao meu principal")

def menu_consulta():
    print("\n===== MENU CONSULTA =====")
    print("1 - Agendar consulta"
          "\n2 - Listar consulta"
          "\n3 - Cancelar consulta"
          "\n4 - Buscar Consulta pelo Codigo"
          "\n0 - Retornar ao meu principal")
def menu():
    while True:
        print("\n===== CLINICA MÉDICA =====")
        print("1 - Paciente"
              "\n2 - Consulta"
              "\n0 - Sair")
        try:
            op = int(input("Digite a opção: "))

            if op == 1:
                while True:
                    menu_paciente()

                    op1 = int(input("Digite a opção: "))

                    if op1 == 1:
                        cadastrar_paciente()
                    elif op1 == 2:
                        listar_pacientes()
                    elif op1 == 3:
                        buscar_paciente_pelo_codigo()
                    elif op1 == 0:
                        print("Retornando ao menu principal....")
                        break
            elif op == 2:
                menu_consulta()

                op2 = int(input("Digite a opção: "))

                if op2 == 1:
                    agendar_consulta()
                elif op2 == 2:
                    listar_consulta()
                elif op2 == 3:
                    cancelar_consulta()
                elif op2 == 4:
                    codigo_consulta = input("Digite o codigo da consulta: ")
                    buscar_consulta_pelo_codigo(codigo_consulta)
                elif op2 == 0:
                    print("Retornando ao menu principal...")
                    break
            elif op == 0:
                print("Finalizando o programa....")
                break
            else:
                print("Digite numeros de 0 a 2")
        except Exception as e:
            print(f"Error{e}")
        except ValueError:
            print("Digite apenas numeros ")
