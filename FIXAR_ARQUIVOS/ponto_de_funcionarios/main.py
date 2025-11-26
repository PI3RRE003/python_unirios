from models import  *

def menu():
    while True:
        print("\n===== TIME CLOCK =======")
        print("1 - Entrada"
              "\n2 - Saida")
        try:
            op = int(input("Digite a opção: "))

            if op == 1:
                ponto_entrada()
            elif op == 2:
                ponto_saida()
            else:
                print("Digite apenas numeros: 1 ou 2")
        except Exception as e:
            print(f"Error:{e}")



menu()