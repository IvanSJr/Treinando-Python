class CarrinhoDeCompras:
    def __init__(self):
        self.produtos = []

    def inserir_produtos(self, produto):
        self.produtos.append(produto)

    def listar_produtos(self):
        for produto in self.produtos:
            print(produto.nome, produto.valor)

    def somar_valor_produtos(self):
        total = 0
        for produto in self.produtos:
            total += produto.valor
        return total


class Produto:
    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor


carrinho = CarrinhoDeCompras()
p1 = Produto('Camiseta 1', 50.50)
p2 = Produto('Camiseta 2', 20.50)
p3 = Produto('Camiseta 3', 30.50)
carrinho.inserir_produtos(p1)
carrinho.inserir_produtos(p2)
carrinho.inserir_produtos(p3)
carrinho.inserir_produtos(p1)
print(carrinho.somar_valor_produtos())
