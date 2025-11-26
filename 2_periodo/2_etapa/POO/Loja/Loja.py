from Produto import Produto

class Loja():
    def __init__(self, nome_loja):
        self.nome_loja = nome_loja
        self.produtos = {}

    def adicionar_produto(self, novo_produto):
        if not isinstance(novo_produto, Produto):
            print("Error: adição inválida")
            return

        if novo_produto in self.produtos:
            print("Error: Produto ja existe na loja")
        