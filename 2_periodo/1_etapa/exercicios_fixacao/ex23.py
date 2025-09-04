catalogo = [
    ['001', 'Arroz 5kg', 25.00],
    ['002', 'Feijão 1kg', 8.50],
    ['003', 'Óleo de Soja 1L', 7.99],
    ['004', 'Leite Integral 1L', 4.80],
    ['005', 'Café 500g', 15.90]
]

carrinho = []

def exibir_catalogo():
    print('\n========== CATALOGO ==========')
    for item in catalogo:
        print(f'{item[0]} - {item[1]} -  {item[2]}')

def adicionar_ao_carrinho():
    print('\n========== ADICIONAR AO CARRINHO ==========')
    for item in catalogo:
        print(f'{item[0]} - {item[1]} -  {item[2]}')
        
    adicionar = input('Digite o codigo(000) para adicionar ao carrinho: ')
    for item in catalogo:    
        if adicionar == item[0]:
            print(f'Item {item[1]} adicionado com sucesso')
            carrinho.append(item)
            break

def calcular_total():
    print('\n========== SOMAR CARRINHO ==========')
    for item in carrinho:
        print(f'{item[0]} - {item[1]} -  {item[2]}')

    total = 0
    for item in carrinho:
        total += item[2]
    print(f'\nTotal a pagar: {total}')


def menu():
    while True:
        print("\n========== PDV ==========")
        print("1 - Exibir Catalogo\
             \n2 - Adicionar ao Carrinho\
             \n3 - Calcular Total\
             \n0 - Sair")
        
        op = int(input('Digite a opção: '))

        if op == 1:
            exibir_catalogo()
        elif op == 2:
            adicionar_ao_carrinho()
        elif op == 3:
            calcular_total()
        elif op == 0:
            print('Encerrando o programa...')
            break

menu()