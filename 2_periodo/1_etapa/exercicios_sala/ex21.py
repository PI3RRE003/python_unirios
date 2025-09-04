produtos = []
def cadastrar_produto():
    codigo = int(input('Digite o codigo de produto: '))
    if buscar_produto(codigo):
        print(f'Produto já existe')
        return
    else:
        nome = input('Digite o nome do produto: ')
        qtd_estoque = int(input('Digite a quantidade do estoque: '))
        produto = [nome, codigo,qtd_estoque]
        produtos.append(produto)
        print(f'Produto:{nome} cadastrado com sucesso')

def buscar_produto(codigo):
    print('\n--------- Buscar produto pelo codigo --------')
    #codigo = int(input('Digite o codigo:'))
    encontrado = False
    
    for produto in produtos:
        if codigo == produto[1]:
            print(f'\nProduto encontrado:\nNome:{produto[0]}\nCodigo:{produto[1]}\nEstoque:{produto[2]} ')
            encontrado = True
            return True
        
    if encontrado == False:
        print('Produto não encontrado na base')

def listar_produtos():
    print('-------- lista dos produtos ---------')
    for produto in produtos:
        print(f'Codigo:{produto[1]}\nNome:{produto[0]}\nEstoque:{produto[2]}')

def realizar_venda():
    print('\n----------- Realizar venda ------------')
    codigo = int(input('Digite o codigo:'))
    encontrado = False
    
    for produto in produtos:
        if produto[1] <= 0:
            print('Estoque zerado verifique a existencia do produto')
        
        if codigo == produto[1]:
            print(f'Produto encontrado:\nNome:{produto[0]}\nCodigo:{produto[1]}\nEstoque:{produto[2]} ')
            qtd_vendida = int(input('Digite a quantidade vendida: '))
            estoque_atualizado =  (produto[2]) - (qtd_vendida) 
            produto[2] = estoque_atualizado
            print(f'\nProduto vendido com sucesso:\nNome:{produto[0]}\nCodigo:{produto[1]}\nEstoque Atualizado:{estoque_atualizado}')
            encontrado = True
                
        
        if encontrado == False:
            print('Produto não encontrado na base')

def main() -> None:
    while True:
        print('\n========== MENU ==========')
        print('1 - CADASTRAR PRODUTO\
               \n2 - BUSCAR PRODUTO\
               \n3 - LISTAR PRODUTOS\
               \n4 - VENDER\
               \n0 - SAIR')
        operador = int(input('Digite a opção desejada: '))

        if operador == 1:
            cadastrar_produto()
        elif operador == 2:
            codigo = int(input('Digite o codigo: '))
            buscar_produto(codigo)
        elif operador == 3:
            listar_produtos()
        elif operador == 4:
            realizar_venda()
        elif operador == 0:
            print('Encerrando programa...')
            break
        else:
            print('Opção inválida')
        

main()