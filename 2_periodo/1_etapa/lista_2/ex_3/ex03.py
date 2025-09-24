from model import * 
def menu_pacinete():
    print("\n========== MENU PACIENTE ==========")
    print("1 - Registrar paciente\
          \n2 - Listar todos pacientes\
          \n3 - Alterar paciente\
          \n0 - Retornar aos menus")

def menu_vacinas():
    print("\n========== MENU VACINA ==========")
    print("1 - Registrar vacina\
          \n2 - Listar vacinas por paciente CPF\
          \n3 - Buscar vacinas pelo codigo\
          \n4 - Listar todas as vacinas\
          \n0 - Retornar aos menus")

def menu():
    while True:
        print("\n========== CONTROLE VACINAS PSF ==========")
        print("1 - Menu paciente\
              \n2 - Menu vacinas\
              \n0 - Sair")
        
        op = int(input("Digite a opção: "))

        if op == 1:
            while True:
                menu_pacinete()
                
                op1 = int(input("Digite a opção: "))

                if op1 == 1:
                    registrar_paciente()
                elif op1 == 2:
                    listar_todos_pacientes()
                elif op1 == 3:
                    cpf = input("Digite o CPF do paciente que deseja alterar: ")
                    alterar_paciente(cpf)
                elif op1 == 0:
                    print("\nRETORNANDO AO MENU PRINCIPAL !!!")
                    break
        
        elif op == 2:
            while True:
                menu_vacinas()

                op2 = int(input("Digite a opção: "))
                
                if op2 == 1:
                    registrar_vacina()
                
                elif op2 == 2:
                    cpf = input("Digite o CPF do paciente para buscar registro de vacinas")
                    listar_vacina_pelo_cpf(cpf)
                
                elif op2 == 3:
                    codigo = input("Digite o codigo da vacina: ")
                    vacinas_pelo_codigo(codigo)
                
                elif op2 == 4:
                    listar_todas_vacinas()
                elif op2 == 0:
                    print("\nRETORNANDO AO MENU PRINCIPAL !!!")
                    break
        
        elif op == 0:
            print("Encerrando o programa....")
            break
        
menu()