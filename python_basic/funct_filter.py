"""
def pares(i):  # função para valores pares
    if i % 2 == 0:
        return i


def impares(i):  # função para valores impares
    if i % 2 == 1:
        return i


lista = [1, 2, 3, 4, 5, 6, 230]
list_impar = filter(impares, lista)
list_par = filter(pares, lista)

print(list_par)  # <filter object at 0x01B9E958> valor iterável.
# Iterando
print(lista)
for par in list_par:
    print(f'Valores pares: {par}')
for impar in list_impar:
    print(f'Valres impares: {impar}')

"""

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


def maior_idade(pessoa):
    if pessoa['idade'] >= 18:
        return pessoa


def menor_idade(pessoa):
    if pessoa['idade'] < 18:
        return pessoa


def filtra(produto1):
    if produto1['preço'] > 50:
        return True


def filtra_alterando(produto2):
    if produto2['preço'] > 50:
        produto2['e_caro'] = True
    return True


# Utilizando lambda
maiores_de_idade = filter(lambda x: x['idade'] >= 18, pessoas)
menores_de_idade = filter(lambda x: x['idade'] < 18, pessoas)
for idade in maiores_de_idade:
    print(idade)

for idade in menores_de_idade:
    print(idade)

# Utilizando função própia
lista_de_maior = filter(maior_idade, pessoas)  # retorna iterável
print(list(lista_de_maior))
lista_de_menor = filter(menor_idade, pessoas)  # retorna iterável
print(list(lista_de_menor))
altera_chave = filter(filtra_alterando, produtos)
for produto in altera_chave:
    print(produto)  # [{'nome': 'p3', 'preço': 50.22, 'e_caro': True}, {'nome': 'p5', 'preço': 51.99, 'e_caro':
    # True}, {'nome': 'p6', 'preço': 52.11, 'e_caro': True}]
verifica_produto_caro = filter(filtra, produtos)  # NÂO FUNCIONANDO POR QUE O DADO JÀ FOI CONSUMIDO!
print(list(verifica_produto_caro))  # [{'nome': 'p3', 'preço': 50.22}, {'nome': 'p5', 'preço': 51.99}...

# Utilziando list comprehension
# idades = [19, 12, 13, 20, 19, 20, 20, 25, 30, 39]
# lista_de_menor2 = [x for x in idades if x < 18]
# lista_de_maior2 = [x for x in idades if x >= 18]
# print(lista_de_menor2)
# print(lista_de_maior2)
