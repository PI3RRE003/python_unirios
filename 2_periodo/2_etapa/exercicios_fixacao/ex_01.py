from models.model_1 import *

def menu():
    while True:
        print("\n========= BANCO MI ========")
        print("1 - Criar Nova Conta"
              "\n2 - Listar todas as contas"
              "\n3 - Realizar deposito"
              "\n4 - Realizar saque"
              "\n5- Sair")

        op = int(input("Digite a opção: "))

        if op == 1:
            criar_nova_conta()
        elif op == 2:
            listar_todas_contas()
        elif op  == 3:
            realizar_deposito()
        elif op == 4:
            realizar_saque()
        elif op == 5:
            print("\nFinalizando o programa...")
            break


menu()

