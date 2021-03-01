"""
# lista são iteraveis mas não são iteradores

Listas, tuplas, str -> sequências -> iteraveis
lista = list(range(10))
print(hasattr(lista, '__iter__'))  # True: significa que é um iteravel
print(hasattr(lista, '__next__'))  # False: significa que não é um iterador
lista = iter(lista)  # adiciona o metodo next ao objeto
print(hasattr(lista, '__next__')) # True: se tornou um iterador
print(next(lista))  # 0
print(next(lista))  # 1
print(next(lista))  # 2
print(next(lista))  # 3
print(next(lista))  # 4
print(next(lista))  # 5
"""

# Geradores - Retornam o próximo valor de um iterável

import time, sys


def gera_fake():
    r = []
    for n in range(100):
        r.append(n)  # Preenchendo a lista
        time.sleep(0.1)
    return r


# Utilizando laço for
def gera():
    for n in range(100):
        yield n
        time.sleep(0.1)


# Sem o laço for
def gera2():
    variavel = 'Valor1'
    yield variavel
    variavel = 'Valor2'
    yield variavel
    variavel = 'Valor3'
    yield variavel


# g_fake = gera_fake()
g = gera()
g2 = gera2()
# for v in g_fake:
#     print(v)
print(hasattr(g, '__next__'))  # True: É um iterador
print(hasattr(g, '__iter__'))  # True: É um iterável
for v in g2:
    print(v)

# Transformando lista em geradores para reduzir o consumo de memória.

lista = [n for n in range(1000)]
print(type(lista))  # <class 'list'>
print(sys.getsizeof(lista))  # Utiliza 4428 bytes de memória
lista = (n for n in range(1000))
print(type(lista))  # <class 'generator'>
print(sys.getsizeof(lista))  # Utiliza 56 byes de memória
