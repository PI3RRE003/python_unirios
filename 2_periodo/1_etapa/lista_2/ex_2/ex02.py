from model import *

def menu():
    while True:
        print("\n============ CADASTRO DE EMPRESAS ==========")
        print("1 - Cadastrar Empresa\
            \n2 - Listar todas Empresas\
            \n3 - Buscar Empresa pelo CNPJ\
            \n4 - Alterar dados da Empresa\
            \n0 - Sair")

        op = int(input("Digite uma opção: "))

        if op == 1:
            cadastrar_empresa()
        elif op == 2:
            listar_todas_empresas()
        elif op == 3:
            cnpj = input("Digite o CNPJ: ")
            buscar_empresa_pelo_cnpj(cnpj)
        elif op == 4:
            cnpj = input("Digite o CNPJ da empresa que deseja alterar: ")
            alterar_dados_da_empresa(cnpj)
        elif op == 0:
            print("FINALIZANDO O PROGRMAMA....")
            break

menu()