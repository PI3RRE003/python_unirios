from datetime import datetime
'''falta adicionar persistencia em csv'''
transacoes = []
def adicionar_transacao():
    print(f"\n{'='*10} Adicionando transação {'='*10}")
    id = "00" + str(gerar_codigo())
    data = datetime.now().strftime("%d/%m/%Y")
    descricao = input("Digite a descrição: ").lower()
    valor = float(input("Digite o valor: "))
    tipo = int(input("\nTipo de despesa:\n1 - Receita\n2 - Despesa\nDigite aqui:"))

    transacao = {
        'id' : id,
        'data' : data,
        'descricao' : descricao,
        'valor' : valor,
        'tipo' : tipo_despesa(tipo)
    }
    transacoes.append(transacao)
    print("\nTRANSAÇÃO ADICIONADA COM SUCESSO !!")
    print(f"ID:{transacao['id']}"
          f"\nData:{transacao['data']}"
          f"\nDescrição:{transacao['descricao']}"
          f"\nValor:{transacao['valor']}"
          f"\nTipo:{transacao['tipo']}")

def gerar_codigo():
    if not transacoes:
        id = 1
    else:
        id = len(transacoes)+1
    return id

def tipo_despesa(tipo):
    if tipo == 1:
        tipo = 'Receita'.lower()
    elif tipo == 2:
        tipo = 'Despesa'.lower()
    return tipo

def listar_todas_transacoes():
    print(f"\n{'=' * 10} Listando transações {'=' * 10}")
    for transacao in transacoes:
        print(f"ID:{transacao['id']}"
              f"\nData:{transacao['data']}"
              f"\nDescrição:{transacao['descricao']}"
              f"\nValor:{transacao['valor']}"
              f"\nTipo:{transacao['tipo']}")

def calcular_saldo_total():
    print(f"\n{'=' * 10} Calculando seu saldo {'=' * 10}")
    total_receita = 0
    total_despesa = 0
    for transacao in transacoes:
        if transacao['tipo'] == "receita":
            total_receita += transacao['valor']
        elif transacao['tipo'] == "despesa":
            total_despesa += transacao['valor']


    saldo_total = total_receita - total_despesa
    print(f"Seu saldo total é de:{saldo_total}")

def listar_por_tipo(tipo):
    print(f"\n{'=' * 10} Listando transação por tipo {'=' * 10}")
    if tipo == 1:
        for transacao in transacoes:
            if transacao['tipo'] == 'receita':
                print(f"\nID:{transacao['id']}"
                      f"\nData:{transacao['data']}"
                      f"\nDescrição:{transacao['descricao']}"
                      f"\nValor:{transacao['valor']}"
                      f"\nTipo:{transacao['tipo']}")
    elif tipo == 2:
        for transacao in transacoes:
            if transacao['tipo'] == 'despesa':
                print(f"\nID:{transacao['id']}"
                      f"\nData:{transacao['data']}"
                      f"\nDescrição:{transacao['descricao']}"
                      f"\nValor:{transacao['valor']}"
                      f"\nTipo:{transacao['tipo']}")
    else:
        print("Erro")

def excluir_transacao(id):
    print(f"\n{'=' * 10} Excluindo transação {'=' * 10}")
    for transacao in transacoes:
        if transacao['id'] == id:
            print("\nTRANSAÇÃO ENCONTRADA !!!")
            print(f"ID:{transacao['id']}"
                  f"\nData:{transacao['data']}"
                  f"\nDescrição:{transacao['descricao']}"
                  f"\nValor:{transacao['valor']}"
                  f"\nTipo:{transacao['tipo']}")

            op = input("Deseja realmente remover? (S/N): ")
            if op.lower() == 's':
                transacoes.remove(transacao)
            elif op.lower() == 'n':
                print("Retornando ao menu.....")
                return
        else:
            print("Error")

def alterar_transacao(id):
    print(f"\n{'=' * 10} Alterando transação {'=' * 10}")
    for transacao in transacoes:
        if transacao['id'] == id:
            print("\nTRANSAÇÃO ENCONTRADA !!!")
            print(f"ID:{transacao['id']}"
                  f"\nData:{transacao['data']}"
                  f"\nDescrição:{transacao['descricao']}"
                  f"\nValor:{transacao['valor']}"
                  f"\nTipo:{transacao['tipo']}")

            op = int(input("Digite o que deseja alterar:"
                           "\n1 - Descrição"
                           "\n2 - Valor"
                           "\n3 - Tipo"
                           "\n0 - Retornar ao menu"))
            if op == 1:
                nova_descricao = input("Digite a nova descrição: ")
                transacao['descricao'] = nova_descricao
            elif op == 2:
                novo_valor = float(input("Digite o novo valor: "))
                transacao['valor'] = novo_valor
            elif op == 3:
                tipo = int(input("Tipo de despesa:\n1 - Receita\n2 - Despesa\nDigite aqui:"))
                transacao['tipo'] = tipo_despesa(tipo)
            elif op == 0:
                print("Retornando ao menu...")
                return
        else:
            print("Error")
