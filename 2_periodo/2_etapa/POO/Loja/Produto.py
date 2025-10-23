class Produto():
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

        if self.quantidade < 0:
            raise ValueError("Error: quantidade não pode ser zero ou negativa")

    def __str__(self):
        produto = (f"\nProduto:{self.nome}"
                   f"\nPreço: R${self.preco:.2f}"
                   f"\nQuantidade:{self.quantidade}")
        return produto

    def adicionar_estoque(self, quantidade_adicionada):
        if quantidade_adicionada <= 0:
            raise ValueError("Error: quantidade não pode ser zero ou negativa")
        else:
            self.quantidade += quantidade_adicionada
            print(f"Quantidade adicionada: {quantidade_adicionada}"
                  f"\nEstoque atualizado:{self.quantidade}")


    def remover_estoque(self, quantidade_removida):
        if quantidade_removida <= 0:
            raise ValueError("Error: quantidade não pode ser zero ou negativa")
        elif quantidade_removida > self.quantidade:
            raise ValueError("Error: quantidade de remoção maior que estoque")
        else:
            self.quantidade -= quantidade_removida
            print(f"Quantidade Removida: {quantidade_removida}"
                  f"\nEstoque atualizado:{self.quantidade}")

    def valor_total_estoque(self):
        total = (self.preco * self.quantidade)
        return total



caneta = Produto("Caneta", 2.50, 10)
valor_total_estoque = caneta.valor_total_estoque()
print(caneta)
print(f"Valor Total do estoque: {valor_total_estoque}")

caneta.remover_estoque(1)
print(caneta)

valor_total_atualizado = caneta.valor_total_estoque()
print(valor_total_atualizado)