from functools import reduce


def soma(x, y):
    return x*y


lista = [2, 2, 3]

soma = reduce(soma, lista)
print(soma)

# Utilizando lambdas

soma_lista = reduce(lambda ac, i: i + ac, lista, 0)
print(soma_lista)

# Utilizando dicionários

produtos = [
    {'nome': 'p1', 'preço': 5.20},
    {'nome': 'p2', 'preço': 15.24},
    {'nome': 'p3', 'preço': 50.22},
    {'nome': 'p4', 'preço': 49.25},
    {'nome': 'p5', 'preço': 51.99},
    {'nome': 'p6', 'preço': 52.11},
    {'nome': 'p7', 'preço': 45.10},
    {'nome': 'p8', 'preço': 40.75},
    {'nome': 'p9', 'preço': 30.80},
    {'nome': 'p10', 'preço': 15.90}
]

# Fazendo a média de preços do produtos

soma_precos = reduce(lambda ac, p: p['preço'] + ac, produtos, 0)
print(soma_precos)  # 356.56
print(round(soma_precos / len(produtos), 2))  # 35.66 é a média de preços dos produtos
