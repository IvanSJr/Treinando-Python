"""
def dobro(x):
    return x * 2


valor = 2

print(dobro(valor))
valor = [2, 5, 2, 5, 1]

print(dobro(valor))  # Vai dobrar a quantidade de números da lista
# map(função, iterável) 2 argumentos a função e a lista

print(list(map(dobro, valor)))

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
nova_lista = map(lambda x: x**2, lista)
print(lista)
print(list(nova_lista))  # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
print(nova_lista)  # <map object at 0x0145E2F8>

# Utilizando list compreehension

nova_lista2 = [x**2 for x in lista]
print(nova_lista2)  # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]


"""

# Utilizando map dicionários

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

pessoas = [
    {'nome': 'Ivan', 'idade': 19},
    {'nome': 'João', 'idade': 12},
    {'nome': 'Maria', 'idade': 13},
    {'nome': 'Sabrina', 'idade': 20},
    {'nome': 'Larissa', 'idade': 19},
    {'nome': 'Evellyn', 'idade': 20},
    {'nome': 'Gustavo', 'idade': 20},
    {'nome': 'Pedro', 'idade': 25},
    {'nome': 'Guilherme', 'idade': 30},
    {'nome': 'Felipe', 'idade': 39}
]


# Aumentando o preço da lista produtos

def aumenta_preco(produto):
    produto['preço'] = round(produto['preço']*1.05, 2)
    return produto


# Retorna uma lista com os preços da lista
precos = map(lambda p: p['preço'], produtos)  # [5.2, 15.24, 50.22, 49.25, 51.99, 52.11, 45.1, 40.75, 30.8, 15.9]
# Alterando os preços
nova_lista = map(aumenta_preco, produtos)  # [{'nome': 'p1', 'preço': 5.46}, {'nome': 'p2', 'preço': 16.0}, {'nome':
# 'p3', 'preço': 52.73}, {'nome': 'p4', 'preço': 51.71}, {'nome': 'p5', 'preço': 54.59}, {'nome': 'p6',
# 'preço': 54.72}, {'nome': 'p7', 'preço': 47.36}, {'nome': 'p8', 'preço': 42.79}, {'nome': 'p9', 'preço': 32.34},
# {'nome': 'p10', 'preço': 16.7}]

print(list(precos))
print(list(nova_lista))