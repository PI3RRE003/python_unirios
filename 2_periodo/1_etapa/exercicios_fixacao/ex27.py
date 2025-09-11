def adicionar_produto():
    print("\n========== ADICIONAR PRODUTO ==========")
    nome = input("Digite o nome do produto: ")
    preco = float(input("Digite o preço do produto: "))
    qtd_estoque = int(input("Digite a quantidade em estoque: "))
    produto = [nome, preco, qtd_estoque]
    produtos.append(produto)
    print(f"Produto:{nome} adicionado com sucesso!!!")

def listar_todos_produtos():
    for produto in produtos:
        print(f"Nome:{produto[0]} - Preço:{produto[1]} - Estoque:{produto[2]}")



produtos = []
def menu():
    while True:
        print('\n============ ESTOQUE ==========')
        print('1 - Adicionar Produto\
              \n2 - Listar todos os produtos\
              \n3 - Atualizar Esstoque\
              \n4 - Buscar Produto por nome\
              \n0 - Sair')
        
        op = int(input("Digite a opção: "))

        if op == 1:
            adicionar_produto()
        elif op == 2:
            listar_todos_produtos()
        elif op == 3:
            atualizar_estoque()
        elif op == 4:
            buscar_por_nome()
        elif op == 0:
            print("Encerrando o programe...")
            break

menu()