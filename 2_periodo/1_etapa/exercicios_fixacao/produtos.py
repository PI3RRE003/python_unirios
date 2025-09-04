class Produto:
    _contador_id = 1
    def __init__(self,nome,preco,estoque):
        self.id = Produto._contador_id
        Produto._contador_id += 1
        self.nome = nome
        self.preco = preco
        self.estoque = estoque

    def get_produto(self):
        return f'ID:{self.id} Nome:{self.nome} - Preço:{self.preco} - Estoque:{self.estoque}'
    
    def get_nome(self):
        return f'{self.nome}'
    
    def set_nome(self, novo_nome):
        self.nome = novo_nome
        return f'Nome atualizado com sucesso:{self.nome}'
    
    def get_preco(self):
        return f'Preço:{self.preco}'
    
    def set_preco(self, novo_preco):
        self.preco = novo_preco
        return f'Preço atualizado com sucesso: {self.preco:.2f}R$'
    
    def get_estoque(self):
        return f'Estoque:{self.estoque}'
    
    def set_estoque(self, nova_quantidade):
        if nova_quantidade > 0:
            self.estoque = nova_quantidade
            return f'Estoque atualizado:{self.estoque}' 
        return f'Quantidade invalida'
    
    @staticmethod
    def atualizar_produto(produtos):
        print('Atualizar Produto')
        for produto in produtos:
            print(f'\n{produto.get_produto()}')
        
        id = int(input('Digite o ID do item que deseja alterar: '))
        for produto in produtos:
            if produto.id == id:
                novo_nome = input('Digite o novo nome:')
                novo_preco = float(input('Digite o novo preço: '))
                nova_quantidade = int(input('Digite a nova quantidae: '))
                produto.set_nome(novo_nome)
                produto.set_preco(novo_preco)
                produto.set_estoque(nova_quantidade)
                print(f'Produto atualizado:{produto.get_produto()}')
                return
        return f'Produto não encontrado'
    
    @staticmethod
    def deletar_produto(produtos):
        print('--- Deletar Produto ---')
        for produto in produtos:
            print(produto.get_produto())
        
        id_busca = int(input('Digite o ID do item que deseja deletar: '))
        for produto in produtos:
            if produto.id == id_busca:
                produtos.remove(produto)
                print(f'Produto {produto.nome} removido com sucesso!')
                return
        print('Produto não encontrado.')

    
    def vender(self, quantidade): 
        if quantidade <= 0:
            print(f'Quantidade inválida')
            return
        if quantidade > self.estoque:
            print('Estoque insuficiente')
            return
        
        self.estoque -= quantidade
        valor_final = (self.preco) * quantidade 
        print(f'Produto:{self.nome}\nPreço:{self.preco}\nQuantidade:{quantidade}\nTotal:{valor_final:.2f}R$\nEstoque restante:{self.estoque}')


produtos = []
def menu():
    while True:
        print('\n----------- PDV ----------\
              \n1 - Cadastrar Produto\
              \n2 - Vizualizar Produtos\
              \n3 - Atualizar Produto\
              \n4 - Deletar produto\
              \n5 - Vender\
              \n0 - Sair')
        operador = int(input('Digite a opção: '))

        if operador == 1:
            nome_produto = input('Digite o nome do produto: ')
            preco_produto = float(input('Digite o preço do produto: '))
            estoque_produto = float(input('Digite a quantidade em estoque: '))
            produto = Produto(nome_produto, preco_produto, estoque_produto)
            produtos.append(produto) 
            print(f'Produto:{produto.get_nome()} cadastrado com sucesso!')
        elif operador == 2:
            for produto in produtos:
                print(f'\n{produto.get_produto()}')
        elif operador == 3:
            Produto.atualizar_produto(produtos)
        elif operador == 4:
            Produto.deletar_produto()
        elif operador == 5:
              for produto in produtos:
                print(produto.get_produto())
                id_busca = int(input('Digite o ID do produto que deseja vender: '))
                for produto in produtos:
                    if produto.id == id_busca:
                        quantidade = int(input('Digite a quantidade: '))
                        produto.vender(quantidade)
                        break
                    else:
                        print("Produto não encontrado.")
        elif operador == 0:
            print('Encerrando o programa....')
            break

menu()