#recebe uma lista e retorna um unico valro para essa lista
from functools import reduce
def soma(x,y):
    return x+y
lista = [1, 2, 3, 5, 66, 775, 634, 654, 243, 53443, 6453]

soma = reduce(soma, lista) # 2 argumentos a função e a lista
print(soma)
