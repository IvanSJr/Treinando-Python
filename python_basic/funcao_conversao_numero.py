import re


def is_float(val):
    if isinstance(val, float): return True
    if re.search(r'^\-{,1}[0-9]+\.{1}[0-9]+$', val): return True

    return False


def is_int(val):
    if isinstance(val, int): return True
    if re.search(r'^\-{,1}[0-9]+$', val): return True

    return False


def is_number(val):
    return is_int(val) or is_float(val)


# Utilizando

n1 = input('Digite um número: ')
n2 = input('Digite outro número: ')


if is_number(n1) and is_number(n2):
    n1 = float(n1)
    n2 = float(n2)
    print(n1+n2)
else:
    print('Não é um número.')