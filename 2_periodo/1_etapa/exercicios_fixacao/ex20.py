def adicionar_funcionarios():
    nome = input('Digite o nome do funcionario: ')
    cargo = input('Digite o cargo do funcionario: ')
    salario = float(input('Digite o salário: '))

    funcionario = [nome, cargo, salario]
    funcionarios.append(funcionario)
    print(f'\nFuncionario:{funcionario[0]}\nCargo:{funcionario[1]}\nSalario:{funcionario[2]}\nCadastrado com sucesso!!!')

def alterar_funcionario():
    for funcionario in enumerate(funcionarios, start=1):
        print(f"{funcionario[0]} - {funcionario[1]}")
    
    alterar_index = int(input('Digite pelo número qual funcionario deseja alterar: '))
    if 1 <= alterar_index <= len(funcionarios):
        funcionario_selecionado = funcionarios[alterar_index - 1]
        
        print(f"Você selecionou: {funcionario_selecionado[0]}")

        novo_nome = input(f"Digite o novo nome (ou pressione Enter para manter '{funcionario_selecionado[0]}'): ")
        novo_cargo = input(f"Digite o novo cargo (ou pressione Enter para manter '{funcionario_selecionado[1]}'): ")
        novo_salario = float(input(f'Digite o novo salario de {funcionario_selecionado[0]}, Salario atual:{funcionario_selecionado[2]}, Novo salario: '))

        if novo_nome:
            funcionario_selecionado[0] = novo_nome
        if novo_cargo:
            funcionario_selecionado[1] = novo_cargo
        if novo_salario:
            funcionario_selecionado[2] = novo_salario

        print(f'\nAtualizado:\nFuncionario:{funcionario_selecionado[0]}\nCargo:{funcionario_selecionado[1]}\nNovo Salario:{funcionario_selecionado[2]}')
    else:
        print("\n❌ Erro: Número inválido. Por favor, escolha um número da lista.")

def remover_funcionario():
     for funcionario in enumerate(funcionarios, start=1):
        print(f"{funcionario[0]} - {funcionario[1]}")
    
     alterar_index = int(input('Digite pelo número qual funcionario deseja remover: '))
     if 1 <= alterar_index <= len(funcionarios):
        funcionario_selecionado = funcionarios[alterar_index - 1]
        
        print(f"Você selecionou: {funcionario_selecionado[0]}")
        funcionarios.remove(funcionario_selecionado)

        print(f'{funcionario_selecionado} Removido com sucesso')

funcionarios = []
def menu():
    while True:
        print("\n========== RH ==========")
        print("1 - Adicionar Funcionario\
            \n2 - Alterar Funcionario\
            \n3 - Remover Funcionario\
            \n4 - Listar Funcionarios\
            \n0 - Sair")
    
        op = int(input('Digite a opção desejada:'))

        if op == 1:
            adicionar_funcionarios()
        elif op == 2:
            alterar_funcionario()
        elif op == 3:
            remover_funcionario()
        elif op == 4:
            print('========== Funcionarios Ativos ==========')
            for funcionario in funcionarios:
                print(f'{funcionario[0]} - {funcionario[1]} - {funcionario[2]}')
        elif op == 0:
            print('Finalizando o programa....')
            break
        


menu()