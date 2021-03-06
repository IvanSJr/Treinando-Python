carrinho = []
carrinho.append(('Produto 1', 30))
carrinho.append(('Produto 2', 10))
carrinho.append(('Produto 3', 20))
carrinho.append(('Produto 4', 50))
carrinho.append(('Produto 5', 30))
total = sum([float(p) for v, p in carrinho])
print(total)
