def mult(a, b):
    return a * b


a = mult(5, 3)
print(a)  # Imprime 15

a = lambda x, y: x * y
print(a(5, 3))  # Imprime 15


produtos = [
    ['P1', 15.09],
    ['P2', 25.19],
    ['P3', 25.59],
    ['P4', 235.09],
    ['P5', 115.00],
    ['P6', 10.00],
    ['P7', 11.09],
]


# def ordenacao(item):
#     return item[1]
#
#
# produtos.sort(key=ordenacao, reverse=False)  # Ordenando por preço
# print(produtos)

# Ordenando lista com lambda

produtos.sort(key=lambda item: item[1], reverse=False)  # Ordenando por preço
print(produtos)

