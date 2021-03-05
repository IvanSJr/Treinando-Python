# Criando modulos em python
# https://docs.python.org/3/tutorial/modules.html
from math import pi

PI = pi


def dobra_lista(lista):
    return [x*2 for x in lista]


def multiplica(lista):
    ac = 1
    for i in lista:
        ac *= i
    return ac


if __name__ == '__main__':
    print(dobra_lista([0, 1, 2, 3, 4, 5]))
    print(multiplica([1, 2, 3, 4, 5]))
    print(PI)