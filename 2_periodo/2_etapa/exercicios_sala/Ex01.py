pessoas = []

def cadastrar():
    print("\n===== CADASTRANDO PESSOA ======")
    try:
        nome = input("Digite o nome do produto: ")

        cpf = input("Informe o CPF: ")
        if buscar(cpf):
            print("Não e possivel cadastrar o mesmo CPF")

        telefone = input("Informe o telefone:")
        pessoa = [nome, cpf, telefone]
        pessoas.append(pessoa)
        print(f"\nPessoa:{pessoa[0]} cadastrada com sucesso")
    except Exception as e:
        print(f"Erro ao cadastrar pessoa: {e}")

def buscar(cpf):
    for pessoa in pessoas:
        if cpf == pessoa[1]:
            print(f"\nPESSOA ENCONTRADA !!!\nNome:{cpf[0]}\nCPF:{cpf[1]}\nTelefone:{cpf[2]}")
            return True
    print(f"Pessoa não cadastrada !!!")
    return False

def listar():
    try:
        if len(pessoas) == 0:
            print("Não há pessoas cadastradas")
        else:
            for pessoa in pessoas:
                print(f"\nNome:{pessoa[0]}\nCPF:{pessoa[1]}\nTelefone:{pessoa[2]}")
    except IndexError as e:
        print(f"Erro de indice: {e}")
    except Exception as e:
        print(f"Error: {e}")

def alterar():
    try:
        cpf = input("Digite o CPF: ")
        if buscar(cpf):
            for pessoa in pessoas:
                try:
                    if cpf == pessoa[1]:
                        print(f"\nPESSOA ENCONTRADA !!!\nNome:{cpf[0]}\nCPF:{cpf[1]}\nTelefone:{cpf[2]}")
                        print("O que deseja alterar?"
                              "\n1 - Nome"
                              "\n2 - CPF"
                              "\n3 - Telefone"
                              "\n0 - Sair")
                        try:
                            op = int(input("Digite a opção: "))
                        except ValueError:
                            print("Erro Digite apenas numeros de 0 a 3")
                            continue

                        if op == 1:
                            novo_nome =input("Digite o novo nome: ")
                            cpf[0] = novo_nome
                        elif op == 2:
                            novo_cpf = input("Digite o novo CPF: ")
                            if buscar(novo_cpf):
                                print("Não e possivel cadastrar o mesmo CPF")
                            else:
                                cpf[1] = novo_cpf
                        elif op == 3:
                            novo_telefone = input("Digite o novo telefone")
                            cpf[2] = novo_telefone
                        elif op == 0:
                            print("Retornando ao menu")
                            return
                        else:
                            print("Opção invalida")
                            continue
                        print("Dados alterados com sucesso")
                except IndexError:
                    print("Error na estruttura de registro da lista")
                except TypeError as e:
                    print(f"Error no tipo de dado:{e}")
        else:
            print("Error: CPF não encontrado")
    except Exception as e:
        print(f"Erro Inesperado: {e}")


def menu():
    print("\n===== MENU =====")
    print("1 - Cadastrar"
          "\n2 - Buscar"
          "\n3 - Listar"
          "\n4 - Alterar"
          "\n0 - Sair")


def main():
    while True:
        try:
            menu()

            op = int(input("Digite a opção: "))

            if op == 1:
                cadastrar()
            elif op == 2:
                cpf = input("Digite o CPF para busca: ")
                buscar(cpf)
            elif op == 3:
                listar()
            elif op == 4:
                alterar()
            elif op == 0:
                print("Saindo do programa...")
                break
            else:
                print("Opção Invalida")
        except ValueError:
            print("\nError: Digite algo valido de 1 a 4")
        except Exception as e:
            print(f"\nOcorreu um erro: {e}")

main()

