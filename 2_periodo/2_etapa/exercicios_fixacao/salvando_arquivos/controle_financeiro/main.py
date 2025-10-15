from model import *
def main():
    while True:
        print(f"\n{'='*10} Sistema de Controle Financeiro Pessoal {'='*10}")
        print("1 - Adicionar Transação"
              "\n2 - Listar Todas as Transações"
              "\n3 - Calcular Saldo total"
              "\n4 - Listar por Tipo"
              "\n5 - Excluir Transação"
              "\n6 - Alterar Transação"
              "\n0 - Sair")

        op = int(input("Digite a opção:"))

        if op == 1:
            adicionar_transacao()
        elif op == 2:
            listar_todas_transacoes()
        elif op == 3:
            calcular_saldo_total()
        elif op == 4:
            tipo = int(input("Digite o tipo que deseja listar:\n"
                             "1 - Receita"
                             "2 - Despesas"))
            listar_por_tipo(tipo)
        elif op == 5:
            id = input("Digite o ID da despesa que deseja remover: ")
            excluir_transacao(id)
        elif op == 6:
            id = input("Digite o ID da despesa que deseja alterar: ")
            alterar_transacao(id)
        elif op == 0:
            print("Finalizando o programa...")
            break

main()