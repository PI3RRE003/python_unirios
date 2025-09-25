contas = []

def criar_nova_conta():
    numero_conta = "00" + str(gerar_codigo())

    titular = input("Digite o nome do titular: ")
    if verifica_titular(titular): return

    saldo = 0.0

    conta = {
        'conta' : numero_conta,
        'titular' : titular,
        'saldo' : saldo
    }
    contas.append(conta)
    print("\nCONTA CADASTRADA COM SUCESSO !!!")
    print(f"Conta:{conta['conta']} - titular:{conta['titular']} - Saldo:{conta['saldo']}")

def gerar_codigo():
    if len(contas) == 0:
        conta = 1
    else:
        conta = len(contas)+1
    return  conta

def verifica_titular(titular):
    if len(titular) == 0:
        print("\nErro: titular não pode ser vazio tente novamente")
        return True
    return False

def verifica_lista_contas():
    if not contas:
        print("\nLista de contas vazia !")
        op = (input("Deseja adicionar uma conta? (S/N): "))
        if op.lower() == 's':
            print("Redirecionando para a criação de contas")
            criar_nova_conta()
            return True
        elif op.lower() == 'n':
            print("Retornando ao menu principal")
            return False
        else:
            print("Opção Invalida digite: (S/N)")
            return False
    return True

def listar_todas_contas():
    prosseguir = verifica_lista_contas()

    if prosseguir:
        print("\n========= LISTANDO TODAS AS CONTAS ===========")
        for conta in contas:
            print(f"Conta:{conta['conta']} - titular:{conta['titular']} - Saldo:{conta['saldo']}")

def realizar_deposito():
    prosseguir = verifica_lista_contas()

    if prosseguir:
        print("\n======== REALIZANDO DEPOSITO ========")
        try:
            numero_conta = input("Digite o numero da conta: ")
        except ValueError:
            print("Verifique numero da conta")
            return

        conta_encontrada = None
        for conta in contas:
            if conta['conta'] == numero_conta:
                conta_encontrada = conta
            else:
                print("Conta não encontrada")
                return

        if conta_encontrada:
            try:
                valor_deposito = float(input(f"\nConta:{conta['conta']}\nDigite o valor do deposito: "))

                if valor_deposito < 0:
                    print("Erro: O valor do deposito deve ser maior que zero")
                    return

                conta_encontrada['saldo'] += valor_deposito
                print("\nDeposito realizado com sucesso !!!")
                print(f"Novo saldo na conta:{conta_encontrada['conta']}: R$:{conta_encontrada['saldo']:.2f}")

            except ValueError:
                print("Erro: valor do deposito inválido. Por favor, digite um numero.")
        else:
            print("Conta não encontrada")

def realizar_saque():
    prosseguir = verifica_lista_contas()

    if prosseguir:
        print("\n======== REALIZANDO SAQUE ========")
        try:
            numero_conta = input("Digite o numero da conta: ")
        except ValueError:
            print("Verifique numero da conta")
            return

        conta_encontrada = None
        for conta in contas:
            if conta['conta'] == numero_conta:
                conta_encontrada = conta
            else:
                print("Conta não encontrada")
                return

        if conta_encontrada:
            try:
                valor_saque = float(input(f"\nConta:{conta['conta']}\nDigite o valor do deposito: "))

                if conta_encontrada['saldo'] < valor_saque:
                    print("Erro: Saque inválido, verifique o valor da sua conta")
                    return

                conta_encontrada['saldo'] -= valor_saque
                print("\nSaque realizado com sucesso !!!")
                print(f"Novo saldo na conta:{conta_encontrada['conta']}: R$:{conta_encontrada['saldo']:.2f}")
            except ValueError:
                print("Erro: verifique o numero da conta")
        else:
            print("Conta não encontrada")
